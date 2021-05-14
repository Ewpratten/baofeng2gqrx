import argparse
import sys
import csv
import os


def main() -> int:

    # Handle program arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("infile", help="Input radio CSV file")
    ap.add_argument("-o", "--outfile",
                    help="Optional output file (if not set, stdout is used)", default="-", required=False)
    ap.add_argument("--simplex-overrides", help="Comma-seperated list of channel prefixes to specify as SIMPLEX",
                    default="VCALL,UCALL,SMPX,ARES", required=False)
    args = ap.parse_args()

    # Ensure valid infile
    if not os.path.isfile(args.infile):
        print(f"Invalid input file: {args.infile}")
        return 1

    # Load the Baofeng file
    baofeng_reader = csv.reader(open(args.infile, "r"))

    # Create an output buffer
    output = []

    # Parse the baofeng file
    for i, row in enumerate(baofeng_reader):
        if i > 0:
            output.append({
                "Name": row[1],
                "Frequency": int(float(row[2]) * 1000000),

                # These are the same for all FM channels
                "Modulation": "Narrow FM",
                "Bandwidth": 10000,

                # The tag depends on the name
                "Tags": "HAM: Simplex" if any([True for prefix in args.simplex_overrides.split(",") if row[1].startswith(prefix)]) else "HAM: Repeaters"
            })

    # Build file contents
    file = """
# AUTO-GENERATED
# Tag name          ;  color
HAM: Simplex; #0394fc
HAM: Repeaters; #fcc203

# Frequency ; Name                     ; Modulation          ;  Bandwidth; Tags
"""
    for entry in output:
        file += "{frequency}; {name}; {modulation}; {bandwidth}; {tags}\n".format(
            frequency=entry["Frequency"], name=entry["Name"], modulation=entry["Modulation"], bandwidth=entry["Bandwidth"], tags=entry["Tags"])

    # Handle output
    if args.outfile == "-":
        print(file)
    else:
        with open(args.outfile, "r") as fp:
            fp.write(file)
        

    return 0


if __name__ == "__main__":
    sys.exit(main())
