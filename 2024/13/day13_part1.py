import re

def play(game):
    max_a = max(game['Prize']['X'] // game['A']['X'], game['Prize']['Y'] // game['A']['Y'])
    max_b = max(game['Prize']['X'] // game['B']['X'], game['Prize']['Y'] // game['B']['Y'])
    for b in range(max_b, 0, -1):
        for a in range(max_a):
            x = game['A']['X'] * a + game['B']['X'] * b
            y = game['A']['Y'] * a + game['B']['Y'] * b
            if x == game['Prize']['X'] and y == game['Prize']['Y']:
                return True, a, b
            if x > game['Prize']['X'] or y > game['Prize']['Y']:
                break

    return False, None, None

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read().strip()

# Regular expression to match numbers after X+, Y+, X=, and Y=
pattern = r'(?:X\+|Y\+|X=|Y=)(\d+)'

# Find all matches
matches = re.findall(pattern, file)

# Format the data
data = []
for chunk in [matches[i:i+6] for i in range(0, len(matches), 6)]:
    data.append({
        "A": {"X": int(chunk[0]), "Y": int(chunk[1])},
        "B": {"X": int(chunk[2]), "Y": int(chunk[3])},
        "Prize": {"X": int(chunk[4]), "Y": int(chunk[5])},
    })

# Process data
total_a = 0
total_b = 0
for game in data:
    found, a, b = play(game)
    if found:
        total_a += a
        total_b += b

tokens = total_a * 3 + total_b
print(tokens)
