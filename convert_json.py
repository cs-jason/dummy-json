# this script takes the format of 10k.json as input and outputs 10k-arrays.json
# it minifies, shortens key names, uses integers instead of floats by multiplying all values by 100 (needs to be divided by 100 when using), uses arrays instead of objects.
import json
import sys

def convert_to_array_format(data):
    result = []
    for item in data:
        name = item['name']
        p = [int(item['pnl'][k] * 100) for k in ['1', '7', '30', '90', '365', 'Lifetime']]
        r = [int(item['roi'][k] * 100) for k in ['1', '7', '30', '90', '365', 'Lifetime']]
        w = [int(item['biggestWin'][k] * 100) for k in ['1', '7', '30', '90', '365', 'Lifetime']]
        result.append([name, {'p': p, 'r': r, 'w': w}])
    return result

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file.json output_file.json")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in input file '{input_file}'.")
        sys.exit(1)

    converted_data = convert_to_array_format(data)

    try:
        with open(output_file, 'w') as f:
            json.dump(converted_data, f, separators=(',', ':'))
        print(f"Converted data written to '{output_file}'")
    except IOError:
        print(f"Error: Unable to write to output file '{output_file}'.")
        sys.exit(1)

if __name__ == "__main__":
    main()