data = [line.split() for line in open(0)]
cols = list(zip(*data))

total = 0

for *nums, op in cols:
    max_len = max(len(num) for num in nums)
    nums = [num.zfill(max_len) for num in nums]
    print(nums)
    values = []

    for length in range(max_len-1, -1, -1):
        values.append(''.join([num[length] for num in nums if len(num) > length and not (num[length] == '0' and len(num) > length)]))
    print(values)
    print(eval(op.join(values)))
    total += eval(op.join(values))

print(total)