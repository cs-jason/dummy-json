import json

# Read the original file
with open('10k_1d.json', 'r') as f:
    data = json.load(f)

# Take the first 1000 traders
reduced_data = data[:1000]

# Write the reduced data to a new file
with open('1k_1d.json', 'w') as f:
    json.dump(reduced_data, f)

print("Reduced data has been written to 1k_1d.json")