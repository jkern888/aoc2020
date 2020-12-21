def part1(inputs):
    preamble_size = 25
    active_set = set(inputs[0:preamble_size])

    for i in range(preamble_size, len(inputs)):
        if not check_for_pair(inputs[i], active_set):
            return inputs[i]

        active_set.remove(inputs[i-preamble_size])
        active_set.add(inputs[i])


def check_for_pair(check_val, active_set):
    for possible in active_set:
        pair = check_val - possible

        if pair != possible and pair in active_set:
            return check_val, possible, pair

    return False

def part2(inputs, target):
    for i in range(0, len(inputs)):
        total = 0
        for j in range(i, len(inputs)):
            total += inputs[j]

            if total == target:
                return min(inputs[i:j]) + max(inputs[i:j])
            elif total > target:
                break

if __name__ == "__main__":
    inputs = [int(line) for line in open("input.txt").readlines()]

    print "part 1:", part1(inputs)
    print "part 2:", part2(inputs, part1(inputs))
