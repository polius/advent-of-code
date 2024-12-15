import re

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read()

# Find matches
pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
matches = re.findall(pattern, file)

enabled = True
result = 0
for operation in matches:
    if operation[0] == "do()":
        enabled = True
    elif operation[0] == "don't()":
        enabled = False
    elif enabled:
        result += int(operation[1]) * int(operation[2])

print(result)