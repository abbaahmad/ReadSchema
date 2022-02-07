import os
import json
import argparse

from GetSchema import parse_data, read_file

def main(args):
    contents = read_file(args.input)
    output = parse_data(contents)
    os.makedirs('schema',exist_ok = True)
    output_filename = os.path.join('schema', args.output)
    print(f'Writing schema to {output_filename}')
    with open(output_filename, 'w') as f:
        json.dump(output,f, indent=4)
    print(f'[INFO] Done')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sniff schema of a give JSON file")
    parser.add_argument("--input", '-i', required=True, type=str, 
						help="JSON filename to parse")
    parser.add_argument("--output", "-o", default="output.json", type=str,
                        help ="Filename of output file to dump schema")
    args = parser.parse_args()
    main(args)