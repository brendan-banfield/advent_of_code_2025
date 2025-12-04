FILEPATH = "input.txt"

def is_roll(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return False
    return grid[i][j] == '@'

def count_neighboring_rolls(grid, i, j):
    neighboring_rolls = 0
    for neighbor_offset in [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]:
        if is_roll(grid, i + neighbor_offset[0], j + neighbor_offset[1]):
            neighboring_rolls += 1
    return neighboring_rolls

def part1():
    with open(FILEPATH) as file:
        grid = [line.strip() for line in file]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '@':
                    continue
                
                if count_neighboring_rolls(grid, i, j) < 4:
                    count += 1
        return count

def part2():
    with open(FILEPATH) as file:
        grid = [list(line.strip()) for line in file]
        rolls = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    rolls.append((i, j))
        count = 0
        last_roll_count = -1
        while len(rolls) != last_roll_count:
            next_rolls = []
            last_roll_count = len(rolls)
            for roll in rolls:
                i, j = roll
                if count_neighboring_rolls(grid, i, j) < 4:
                    grid[i][j] = '.'
                    count += 1
                else:
                    next_rolls.append(roll)
            rolls = next_rolls
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