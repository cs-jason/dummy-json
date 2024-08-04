import json
import sys

def create_timeframe_file(data, timeframe, index):
    result = []
    for item in data:
        name = item['name']
        pnl = int(item['pnl'][timeframe] * 100)
        roi = int(item['roi'][timeframe] * 100)
        biggestWin = int(item['biggestWin'][timeframe] * 100)
        result.append([name, pnl, roi, biggestWin])
    
    filename = f"{timeframe}_days.json"
    if timeframe == 'Lifetime':
        filename = "lifetime.json"
    elif timeframe == '1':
        filename = "1_day.json"
    
    with open(filename, 'w') as f:
        json.dump(result, f, separators=(',', ':'))
    print(f"Created {filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file.json")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in input file '{input_file}'.")
        sys.exit(1)

    timeframes = ['1', '7', '30', '90', '365', 'Lifetime']
    for index, timeframe in enumerate(timeframes):
        create_timeframe_file(data, timeframe, index)

if __name__ == "__main__":
    main()