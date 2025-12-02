FILEPATH = "input.txt"

def part1():
    output = 0
    with open(FILEPATH) as file:
        ranges = file.read().split(",")
        for r in ranges:
            start, end = r.split('-')
            for n in range(int(start), int(end) + 1):
                s = str(n)
                l = len(s)
                if l % 2 == 1:
                    continue
                if s[:int(l/2)] == s[int(l/2):]:
                    output += n
    return output


def part2():
    output = 0
    with open(FILEPATH) as file:
        ranges = file.read().split(",")
        for r in ranges:
            start, end = r.split('-')
            for n in range(int(start), int(end) + 1):
                s = str(n)
                l = len(s)

                # since all numbers in the input are short, we don't need to do any fancy factorization techniques
                for substring_length in range(1, l // 2 + 1):
                    if l % substring_length != 0:
                        continue
                    if s == s[:substring_length] * int(l / substring_length):
                        output += n
                        break
                        break

    return output


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