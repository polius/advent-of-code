data = [tuple(map(int, line.split(','))) for line in open(0)]

max_area = 0

for x1, y1, in data:
    for x2, y2 in data:
        max_area = max(max_area, abs(x2 - x1 + 1) * abs(y2 - y1 + 1))

print(max_area)