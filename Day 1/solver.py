FILEPATH = "input.txt"
DIAL_SIZE = 100
INITIAL_DIAL_POSITION = 50


def part1():
    dial_position = INITIAL_DIAL_POSITION
    output = 0
    with open(FILEPATH) as file:
        for line in file:
            direction = line[0]
            steps = int(line[1:])
            if direction == 'R':
                dial_position += steps
            else:
                dial_position -= steps
            dial_position = dial_position % DIAL_SIZE
            if dial_position == 0:
                output += 1
        return output

def part2():
    dial_position = INITIAL_DIAL_POSITION
    output = 0
    with open(FILEPATH) as file:
        for line in file:
            direction = line[0]
            steps = int(line[1:])
            if direction == 'R':
                dial_position += steps

                # if we've gone past DIAL_SIZE, add 1 to output for each time we passed it
                output += int(dial_position // DIAL_SIZE)

                # # subtract how far left of 0 we are
                # if dial_position + steps >= DIAL_SIZE:
                #     # will result in at least one tick by 0
                #     output += 1

                #     steps_overshot = dial_position + steps - DIAL_SIZE
                #     output += int(steps_overshot // DIAL_SIZE)

                # dial_position += steps
            else:
                # this case needs special handling. In the rightwards turn case, we never start at 100,
                # but here if we start at 0 it looks like we passed 0 when we actually did not
                if dial_position == 0:
                    output -= 1

                dial_position -= steps
                # "correct" the dial position down by 100 before taking the abs to see how many times it passed 0
                output += int(abs(dial_position - 100) // DIAL_SIZE)

            # return the dial position to the allowed range
            dial_position = dial_position % DIAL_SIZE
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