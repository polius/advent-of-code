def is_safe(report):
    # Check if levels are either all increasing or all decreasing 
    if sorted(report) == report or sorted(report, reverse=True) == report:
        # Check adjacent levels
        if all(1 <= abs(current_value - next_value) <= 3 for current_value, next_value in zip(report, report[1:])):
            return True

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read()

# Initialize vars
safe_reports = 0

# Iterate file
for line in file.split('\n'):
    report = [int(value) for value in line.split()]
    if len(report) == 0:
        continue

    # Check if the report is safe as is
    if is_safe(report):
        safe_reports += 1
    else:
        for i in range(len(report)):
            new_report = report[:i] + report[i + 1:]
            if is_safe(new_report):
                safe_reports += 1
                break

# Print safe reports
print(safe_reports)