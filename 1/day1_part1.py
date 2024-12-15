# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read()

# Initialize variables
first_list = []
second_list = []
distance = 0

# Extract values
for line in file.split('\n'):
    values = line.split()
    if len(values) == 2:
        first_list.append(values[0])
        second_list.append(values[1])

# Order lists
first_list.sort()
second_list.sort()

# Calculate distance
while len(first_list) > 0:
    distance += abs(int(first_list.pop(0)) - int(second_list.pop(0)))

# Print distance
print(distance)