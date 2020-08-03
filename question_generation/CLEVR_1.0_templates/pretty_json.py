import argparse
import json

parser = argparse.ArgumentParser(description="Pretty prints a json file")

parser.add_argument('input_file', metavar='input_file', type=str, help='Input json file')
parser.add_argument('output_file', metavar='output_file', type=str, help='Output json file')

args = parser.parse_args()

file_name = args.input_file
file_to_save = args.output_file

f = open(file_to_save, 'w')

with open(file_name, 'r') as handle:
    parsed = json.load(handle)
    f.write(json.dumps(parsed, ensure_ascii=True, indent=4, sort_keys=True))