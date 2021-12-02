data = [(line.split()[0], int(line.split()[1])) for line in open("d2.data")]


def part1():
    horizontal = 0
    depth = 0

    for direction, value in data:
        if direction == "forward":
            horizontal += value
        elif direction == "down":
            depth += value
        elif direction == "up":
            depth -= value
        else:
            print(direction)
    print(horizontal, depth, horizontal * depth)

def part2():
    horizontal = 0
    aim = 0
    depth = 0

    for direction, value in data:
        if direction == "forward":
            horizontal += value
            depth += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
    print(horizontal, depth, horizontal * depth)



part2()
