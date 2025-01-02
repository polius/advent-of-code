def check(design, towels):
    if design == '':
        return True
    
    for t in towels:
        if design.startswith(t):
            if check(design[len(t):], towels):
                return True
    return False

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read().strip()

towels = sorted([i.strip() for i in file.split('\n\n')[0].split(',')], key=len, reverse=True)
designs = file.split('\n\n')[1].split('\n')

result = {k: False for k in designs}

for d in designs:
    result[d] = check(d, towels)

print(sum(1 if i else 0 for i in result.values()))