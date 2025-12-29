data = [tuple(map(int, i.split(','))) for i in open(0)]
distances = []
circuits = []

for i, n in enumerate(data):
    for j, m in enumerate(data):
        if i < j:
            distances.append({
                "point1": n,
                "point2": m,
                "distance": (n[0]-m[0])**2 + (n[1]-m[1])**2 + (n[2]-m[2])**2
            })

distances.sort(key=lambda x: x["distance"])

attempts = 0
for i in distances:
    attempts += 1
    if attempts > 1000: # 10 for example.txt and 1000 for input.txt
        break

    pos1_idx = next((pos for pos, c in enumerate(circuits) if i["point1"] in c), None)
    pos2_idx = next((pos for pos, c in enumerate(circuits) if i["point2"] in c), None)

    if pos1_idx is None and pos2_idx is None:
        circuits.append([i["point1"], i["point2"]])

    elif pos1_idx is not None and pos2_idx is not None and pos1_idx != pos2_idx:
        circuits[pos1_idx].extend(circuits[pos2_idx])
        del circuits[pos2_idx]

    elif pos1_idx is not None and pos2_idx is None:
        circuits[pos1_idx].append(i["point2"])

    elif pos1_idx is None and pos2_idx is not None:
        circuits[pos2_idx].append(i["point1"])

sizes = sorted([len(c) for c in circuits], reverse=True)[:3]

total = 1
for s in sizes:
    total *= s

print(total)