# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read().strip()

# Init data variable
data = []

# Expand data
identifier = 0
for pos, char in enumerate(file):
    if pos % 2 == 0:
       data.extend([[str(identifier)] for _ in range(int(char))])
       identifier += 1
    else:
        data.extend([['.'] for _ in range(int(char))])

# print(''.join([char[0] for char in data]))

# Dense data
dot = 0
for i in reversed(range(len(data))):
    if data[i][0] == '.':
        continue

    while dot < i and data[dot][0] != '.':
        dot += 1

    if dot >= i:
        break

    data[dot][0], data[i][0] = data[i][0], '.'
    dot += 1

# print(''.join([char[0] for char in data]))

# Compute checksum
checksum = 0
for pos, char in enumerate(data):
    if char[0] != '.':
        checksum += pos * int(char[0])

print(checksum)