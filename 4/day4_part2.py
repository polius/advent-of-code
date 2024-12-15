def check_word(word, target):
    return word == target or word[::-1] == target

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read()

text = [list(line) for line in file.split('\n') if len(line) != 0]
target = 'MAS'
matches = 0

for x in range(1, len(text) - 1):
    for y in range(1, len(text[x]) - 1):
        if text[x][y] == 'A':
            left_right_diagonal = ''.join(text[x - 1 + i][y - 1 + i] for i in range(3))
            right_left_diagonal = ''.join(text[x + 1 - i][y - 1 + i] for i in range(3))

            # Check if both diagonals match the target
            if check_word(left_right_diagonal, target) and check_word(right_left_diagonal, target):
                matches += 1

print(matches)