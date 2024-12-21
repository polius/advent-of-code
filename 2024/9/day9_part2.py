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

# Dense data
end = None
for i in reversed(range(len(data))):
    if end is None and data[i][0] != '.':
        end = i

    if end is not None and i - 1 >= 0 and data[i-1][0] != data[end][0]:
        start = None
        for j in range(end):
            if start is None and data[j][0] == '.':
                start = j

            if data[j][0] == '.':
                if j - start == end - i:
                    for x in range(start, j+1):
                        data[x][0] = data[end][0]
                    for x in range(i, end+1):
                        data[x][0] = '.'
                    break
            else:
                start = None
        end = None

# Compute checksum
checksum = 0
for pos, char in enumerate(data):
    if char[0] != '.':
        checksum += pos * int(char[0])

print(checksum)