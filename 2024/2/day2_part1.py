# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read()

# Initialize vars
safe_reports = 0

# Iterate file
for line in file.split('\n'):
    report = [int(value) for value in line.split()]

    # Check if levels are either all increasing or all decreasing 
    if len(report) != 0 and (sorted(report) == report or sorted(report, reverse=True) == report):
        # Check adjacent levels
        if all(1 <= abs(current_value - next_value) <= 3 for current_value, next_value in zip(report, report[1:])):
            safe_reports += 1

# Print safe reports
print(safe_reports)