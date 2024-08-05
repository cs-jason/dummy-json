import random
import json

def load_words(file_path):
    with open(file_path, 'r') as f:
        return [word.strip() for word in f if len(word.strip()) == 5]

def generate_name(words):
    return "-".join(random.sample(words, 3))

# Load 5-letter words from a file
words = load_words('/Users/jason/Local/Code/Github Repos/dummy-json/five-letter-words.txt')

# Generate 1000 names
names = [generate_name(words) for _ in range(1000)]

# Save to JSON file
with open('random_names.json', 'w') as f:
    json.dump(names, f, indent=2)

print("1000 random names have been generated and saved to 'random_names.json'")