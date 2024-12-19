def check_word(word, target):
    return word == target or word[::-1] == target

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read()

text = [list(line) for line in file.split('\n') if len(line) != 0]
target = 'XMAS'
matches = 0

for x in range(len(text)):
    for y in range(len(text[x])):
        # Right
        if y + 3 < len(text[x]):
            word = ''.join(text[x][y + i] for i in range(4))
            if check_word(word, target):
                matches += 1

        # Diagonal (Right to Down)
        if x + 3 < len(text) and y + 3 < len(text[x]):
            word = ''.join(text[x + i][y + i] for i in range(4))
            if check_word(word, target):
                matches += 1

        # Down
        if x + 3 < len(text):
            word = ''.join(text[x + i][y] for i in range(4))
            if check_word(word, target):
                matches += 1

        # Diagonal (Down to Left)
        if x + 3 < len(text) and y - 3 >= 0:
            word = ''.join(text[x + i][y - i] for i in range(4))
            if check_word(word, target):
                matches += 1

print(matches)