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

incorrect_updates = []
correct_updates = []

# Find incorrect updates
for update in updates:
    for position, value in enumerate(update):
        if not all(i in rules[value] for i in update[position+1:]):
            incorrect_updates.append(update)
            break

# Fix incorrect updates
for update in incorrect_updates:
    levels = {}
    for value in update:
        levels[value] = [int(i) for i in update if i in rules[value]]
    correct_updates.append(sorted(levels, key=lambda k: len(levels[k]), reverse=True))

# Show middle page for all fixed incorrect updates
sum_correct_updates = sum(int(i[len(i) // 2]) for i in correct_updates)
print(sum_correct_updates)
