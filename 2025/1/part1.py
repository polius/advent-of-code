data = [int(line.strip().replace('R','').replace('L','-')) for line in open(0)]

password = 0
dial = 50

for val in data:
    dial = (dial + val) % 100
    if dial == 0:
        password += 1

print(password)