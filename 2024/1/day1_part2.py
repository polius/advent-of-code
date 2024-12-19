# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read()

# Initialize variables
first_list = []
second_list = {}
similarity = 0

# Extract values
for line in file.split('\n'):
    values = line.split()
    if len(values) == 2:
        first_list.append(values[0])
        second_list[values[1]] = second_list.get(values[1], 0) + 1

# Calculate similarity
for value in first_list:
    similarity += int(value) * int(second_list.get(value, 0))

# Print distance
print(similarity)