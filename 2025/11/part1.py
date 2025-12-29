from functools import cache

data = {line.split(':')[0]: line.split(':')[1].split() for line in open(0)}

@cache
def traverse(key):
    if key == 'out': return 1
    return sum(traverse(i) for i in data[key])

print(traverse('you'))