def part1(inputs):
    ones, threes = 0,0

    for i in range(1, len(inputs)):
        diff = inputs[i] - inputs[i-1] 
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1

    return ones, threes, ones * threes

def part2(inputs, results):
    if len(inputs) == 1:
        return 1
    elif inputs[0] in results:
        return results[inputs[0]]

    combinations = 0
    start = inputs[0]

    for i in range(1, min(len(inputs), 4)):
        if inputs[i] - start <= 3:
            combinations += part2(inputs[i:], results)

    results[start] = combinations
    return combinations

if __name__ == "__main__":
    inputs = sorted([int(line) for line in open("input.txt").readlines()])
    inputs = [0] + inputs + [inputs[len(inputs)-1] + 3]

    print "part 1:", part1(inputs)
    print "part 2:", part2(inputs, {})
