FILEPATH = "input.txt"

def part1():
    with open(FILEPATH) as file:
        ranges = []
        lines = [line.strip() for line in file]
        empty_idx = lines.index("")
        ranges = [[int(n) for n in line.split("-")] for line in lines[:empty_idx]]
        ingredients = [int(n) for n in lines[empty_idx + 1:]]     

        # since the number of ranges is not very large, it's not necessary to do anything fancy with
        # sorting and consolodating ranges. Checking each range for every ingredient is good enough
        fresh_count = 0
        for ingredient in ingredients:
            is_fresh = False
            for range in ranges:
                if range[0] <= ingredient <= range[1]:
                    is_fresh = True
                    break
            if is_fresh:
                fresh_count += 1
        return fresh_count
        

def part2():
    with open(FILEPATH) as file:
        ranges = []
        lines = [line.strip() for line in file]
        empty_idx = lines.index("")
        ranges = [[int(n) for n in line.split("-")] for line in lines[:empty_idx]]
        # sort the ranges to have ascending starts, allowing us to only worry about increasing ingredient numbers
        ranges.sort()

        count = 0
        max_counted = 0
        # iterate over the ranges and track the largest number we've seen
        # Since we sorted the array, this is all we need to keep track of from prior ranges
        for range in ranges:
            start, end = range
            if end <= max_counted:
                continue
            if start > max_counted:
                count += end - start + 1
                max_counted = end
            else:
                count += end - max_counted
                max_counted = end
        return count

        

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