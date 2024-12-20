from itertools import product

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read()

# Build data
data = []
for line in file.split('\n'):
    if line.strip():
        raw = line.split(':')
        data.append((int(raw[0]), [int(i) for i in raw[1].strip().split(' ')]))

calibrations = 0
for i, item in enumerate(data):
    print(f"Processing {i+1}/{len(data)}")
    # Extract item
    test, numbers = item

    # Build combinations
    combinations = product(['+', '*', '||'], repeat=len(numbers) - 1)

    # For each combination of operators, build the expression
    for ops in combinations:
        compute = numbers[0]
        for num, op in zip(numbers[1:], ops):
            if op == '||':
                compute = int(str(compute) + str(num))
            elif op == '+':
                compute += num
            elif op == '*':
                compute *= num

            if compute > test:
                break

        if compute == test:
            calibrations += test
            break

print(calibrations)