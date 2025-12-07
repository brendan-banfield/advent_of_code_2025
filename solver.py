FILEPATH = "input.txt"
import numpy as np


def part1():
    with open(FILEPATH) as file:
        # parse the file and remove all whitespace
        grid = [[s for s in line.strip().split(" ") if s] for line in file]

        total = 0
        for column in range(len(grid[0])):

            op = grid[-1][column]
            contribution = int(grid[0][column])
            # sum over the line to find the result of the equation
            for row in grid[1:-1]:
                if op == "+":
                    contribution += int(row[column])
                elif op == "*":
                    contribution *= int(row[column])
            # add equation result to total
            total += contribution
        return total

        

def part2():
    with open(FILEPATH) as file:
        lines = [line[:-1] for line in file]
        ops = [s for s in lines[-1].split(" ") if s]

        # add whitespace to make all lines the same length to allow numpy transposition
        max_line_len = max(len(line) for line in lines[:-1])
        chars = [list(line) + [""] * (max_line_len - len(line)) for line in lines[:-1]]

        # swap axes
        transposed = np.transpose(chars)
        
        nums = [[s for s in ("".join(line)).split(" ") if s] for line in transposed]
        total = 0
        num_idx = 0
        for op in ops:
            contribution = 1 if op == "*" else 0
            while num_idx < len(nums) and nums[num_idx]:
                if op == "+":
                    contribution += int(nums[num_idx][0])
                elif op == "*":
                    contribution *= int(nums[num_idx][0])
                num_idx += 1
            num_idx += 1
            total += contribution
        
        return total
        

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