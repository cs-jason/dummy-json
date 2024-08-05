import json

# Load the random names
with open('random_names.json', 'r') as f:
    random_names = json.load(f)

# Load the 1k_life data
with open('1k_life.json', 'r') as f:
    data = json.load(f)

# Replace names in the 1k_life data
for i, item in enumerate(data):
    if i < len(random_names):
        item[0] = random_names[i]
    else:
        print(f"Warning: Not enough random names to replace all items. Stopped at index {i}")
        break

# Save the updated data back to 1k_life.json
with open('1k_life2.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Names have been replaced and saved to '1k_life2.json'")