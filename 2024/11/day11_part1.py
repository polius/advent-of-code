def blink(data):
    # Base case: when there's only one element
    if len(data) == 1:
        item = data[0]
        if item == '0':
            return ['1']
        elif len(item) % 2 == 0:
            mid = len(item) // 2
            return [item[:mid], str(int(item[mid:]))]
        else:
            return [str(int(item) * 2024)]

    # Recursive case: split data into halves
    mid = len(data) // 2
    left_result = blink(data[:mid])
    right_result = blink(data[mid:])
    return left_result + right_result

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read().strip()

data = file.split(' ')

for i in range(25):
    data = blink(data)

print(len(data))
