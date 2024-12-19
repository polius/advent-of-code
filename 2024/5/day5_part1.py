# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read()

rules = {}
updates = []

# Extract information
for line in file.split('\n'):
    if '|' in line:
        first, second = line.split('|')
        rules[first] = rules.get(first, []) + [second]
    elif ',' in line:
        updates.append(line.split(','))

correct_updates = []

for update in updates:
    valid = True
    for position, value in enumerate(update):
        if not all(i in rules[value] for i in update[position+1:]):
            valid = False
            break
    if valid:
        correct_updates.append(update)

sum_correct_updates = sum(int(i[len(i) // 2]) for i in correct_updates)
print(sum_correct_updates)
