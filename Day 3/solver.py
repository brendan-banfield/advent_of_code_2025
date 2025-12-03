FILEPATH = "input.txt"

def part1():
    total_joltage = 0
    with open(FILEPATH) as file:
        for line in file:
            n1 = n2 = 0
            stripped_line = line.strip()
            for i, char in enumerate(stripped_line):
                n = int(char)
                if i < len(stripped_line) - 1:
                    if n > n1:
                        n1 = n
                        n2 = 0
                    elif n > n2:
                        n2 = n
                else:
                    n2 = max(n2, n)
            joltage = n1 * 10 + n2
            total_joltage += joltage
    return total_joltage

def part2():
    total_joltage = 0
    with open(FILEPATH) as file:
        for line in file:
            stripped_line = line.strip()
            digits = [0] * 12
            for i, char in enumerate(stripped_line):
                n = int(char)

                # if we are less than 12 digits from the end, consider all 12 places
                # otherwise, consider only the 12 - (distance from end)
                num_allowed_places = min(12, len(stripped_line) - i)
                for allowed_digit in range(12 - num_allowed_places, 12):

                    if digits[allowed_digit] < n:
                        # if we found an improvement, reset all later digits since we're now using a digit that comes after them in the line
                        digits[allowed_digit] = n
                        for digit in range(allowed_digit + 1, 12):
                            digits[digit] = 0
                        break
            # lazy way to combine the digits
            joltage = int("".join([str(digit) for digit in digits]))
            total_joltage += joltage
    return total_joltage
                


if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) == 1:
        print(f"Part 1 result: {part1()}")
        print(f"Part 2 result: {part2()}")
    elif args[1] == "1":
        print(f"Part 1 result: {part1()}")
    elif args[1] == "2":
        print(f"Part 2 result: {part2()}")
    else:
        print('Invalid usage. Valid command line arguments are "1" or "2"')