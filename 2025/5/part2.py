ranges = [tuple(map(int, line.split('-'))) for line in open(0).read().split('\n\n')[0].splitlines()]
ranges.sort()

count = 0
last = tuple(ranges[0])

for lo, hi in ranges[1:]:
    if last[1] < lo:
        count += last[1] - last[0] + 1
        last = (lo, hi)
    else:
        last = (last[0], max(last[1], hi))

count += last[1] - last[0] + 1
print(count)