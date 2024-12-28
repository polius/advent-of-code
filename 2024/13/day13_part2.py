import re

# Using Cramer's Rule
# X * a1 + Y * b1 = c1
# X * a2 + Y * b2 = c2
def play(game):
    # Step 1: Calculate Determinants
    # D = a1 * b2 - a2 * b1
    D = game['A']['X'] * game['B']['Y'] - game['B']['X'] * game['A']['Y']

    if D == 0:
        return 0  # No solution

    # Step 2: Calculate Determinant Dx
    # Dx = c1 * b2 - c2 * b1
    Dx = game['Prize']['X'] * game['B']['Y'] - game['Prize']['Y'] * game['B']['X']

    # Step 3: Calculate Determinant Dy
    # Dy = a1 * c2 - a2 * c1
    Dy = game['A']['X'] * game['Prize']['Y'] - game['A']['Y'] * game['Prize']['X']

    # Step 4. Solve A and B
    # A = Dx / D
    # B = Dy / D
    A = Dx / D
    B = Dy / D

    # Step 5: Check if A and B are integers
    if A.is_integer() and B.is_integer():
        return int(A) * 3 + int(B)

    return 0

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
        "Prize": {"X": int(chunk[4]) + 10000000000000, "Y": int(chunk[5]) + 10000000000000},
    })

# Process data
tokens = 0
for game in data:
    tokens += play(game)

print(tokens)
