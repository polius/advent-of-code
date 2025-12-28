data = [line.split() for line in open(0)]
cols = list(zip(*data))

total = 0

for num, *nums, op in cols:
    print(num, nums, op)

    # total += eval(op.join(nums))

# print(total)