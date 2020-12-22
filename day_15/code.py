def part1(inputs, iters):
    nums = [int(num) for num in inputs.split(",")]
    positions = {}
    
    for i in range(1, iters+1):
        val = nums.pop(0)

        if not nums:
            if val not in positions:
                nums.append(0)
            else:
                nums.append(i - positions[val])

        positions[val] = i

    return val

def part2(inputs):
    return part1(inputs, 30000000)

if __name__ == "__main__":
    inputs = [line.strip() for line in open("input.txt").readlines()][0]

    print "part 1:", part1(inputs, 2020)
    print "part 2:", part2(inputs)
