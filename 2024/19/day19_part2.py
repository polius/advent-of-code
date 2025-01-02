from functools import cache

@cache
def count(design, towels):
    if design == '':
        return 1

    result = 0
    for t in towels:
        if design.startswith(t):
            result += count(design[len(t):], towels)

    return result

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read().strip()

towels = [i.strip() for i in file.split('\n\n')[0].split(',')]
designs = file.split('\n\n')[1].split('\n')

result = sum(count(d, tuple(towels)) for d in designs)
print(result)
