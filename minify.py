import json
import sys

def minify_json(input_file, output_file):
    try:
        # Read the input JSON file
        with open(input_file, 'r') as f:
            data = json.load(f)

        # Write the minified JSON to the output file
        with open(output_file, 'w') as f:
            json.dump(data, f, separators=(',', ':'))

        print(f"Successfully minified {input_file} to {output_file}")
    except json.JSONDecodeError:
        print(f"Error: {input_file} is not a valid JSON file")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python minify_json.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        minify_json(input_file, output_file)