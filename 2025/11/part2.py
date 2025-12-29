from functools import cache

data = {line.split(':')[0]: line.split(':')[1].split() for line in open(0)}

@cache
def traverse(key, fft=False, dac=False):
    if key == 'out': return fft and dac
    return sum(traverse(i, fft or key == 'fft', dac or key == 'dac') for i in data[key])

print(traverse('svr'))