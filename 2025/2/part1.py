def split_middle(string):
    s = str(string)
    mid = len(s) // 2
    return s[:mid], s[mid:]

def main():
    # Read input data and parse it
    with open("input.txt") as f:
        data = [list(map(int, value.split('-'))) for value in f.read().strip().split(',')]
    
    # Initialize variables
    invalid = 0

    for start, end in data:
        for num in range(start, end + 1):
            first, second = split_middle(num)
            if len(first) == len(second) and first == second:
                invalid += num

    # Output the count of invalid ranges
    print(invalid)

if __name__ == "__main__":
    main()
