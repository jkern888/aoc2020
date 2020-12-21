def part1_2(inputs, slopes):
    return reduce(lambda x, y: x * y, [solve(inputs, slope) for slope in slopes])

def solve(inputs, slope):
    trees = 0

    for i, y in enumerate(range(0, len(inputs), slope[1])):
        x = (slope[0] * i) % len(inputs[0])

        if inputs[y][x] == "#":
            trees += 1

    return trees        

if __name__ == "__main__":
    inputs = [line.strip() for line in open("input.txt").readlines()]

    print "part 1:", part1_2(inputs, [(3,1)])
    print "part 2:", part1_2(inputs, [(1,1), (3,1), (5,1), (7,1), (1,2)])
