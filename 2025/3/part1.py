total = 0

for line in open(0):
    bank = list(map(int, line.strip()))
    first = max(bank[:-1])
    second = max(bank[bank.index(first) + 1:])
    total += first * 10 + second

print(f"Total jolts: {total}")