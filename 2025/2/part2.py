def check(text, num_parts):
    # Get the size of each part and remainder
    div, mod = divmod(len(text), num_parts)

    # If it doesn't divide evenly, it's valid
    if mod != 0:
        return True

    # Split the text into parts
    parts = []
    for i in range(div):
        start = i * num_parts
        end = start + num_parts
        parts.append(text[start:end])

    # Return if the text is valid
    return len(set(parts)) != 1 or parts[0] == text

def main():
    data = [list(map(int, value.split('-'))) for value in open(0).read().strip().split(',')]
    invalid = 0

    for start, end in data:
        for num in range(start, end + 1):
            is_valid = all(check(str(num), part) for part in range(1, len(str(num)) // 2 + 1))
            if not is_valid:
                invalid += num

    print(invalid)

if __name__ == "__main__":
    main()
