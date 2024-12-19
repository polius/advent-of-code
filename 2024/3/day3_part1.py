import re

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read()

# Capture the numbers inside mul()
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
matches = re.findall(pattern, file)

# Calculate operations
result = sum(int(x) * int(y) for x, y in matches)
print(result)
