data = [int(line.strip().replace('R','').replace('L','-')) for line in open(0)]

password = 0
dial = 50

for val in data:
    if val > 0:
        div, mod = divmod(val, 100)
        password += div
        if dial + mod >= 100:
            password += 1

    elif val < 0:
        div, mod = divmod(val, -100)
        password += div
        if dial > 0 and (dial + mod) <= 0:
            password += 1

    dial = (dial + val) % 100

print(password)