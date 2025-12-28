ranges, numbers = open(0).read().split('\n\n')

ranges = [list(map(int, line.split('-'))) for line in ranges.splitlines()]
numbers = list(map(int, numbers.splitlines()))

total = sum(1 for i in numbers if any(i >= group[0] and i <= group[1] for group in ranges))
print(total)