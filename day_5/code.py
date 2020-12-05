def part1(inputs):
    return map(find_seat_id, inputs)    

def part2(inputs):
    ids = sorted(part1(inputs))

    for i in range(0, len(ids) -1):
        if ids[i + 1] != ids[i] + 1:
            return ids[i] + 1

def find_seat_id(code):
    row = bsearch(code[:7], 0, 127, "F")
    seat = bsearch(code[7:], 0, 7, "L") 
    return row * 8 + seat

def bsearch(code, low, high, split_val):
    for r in code:
        midpoint = (high-low)/2
        if r == split_val:
            high = low + midpoint
        else:
            low = high - midpoint

    return low if r == split_val else high


if __name__ == "__main__":
    inputs = [line.strip() for line in open("input.txt").readlines()]

    print "part 1:", max(part1(inputs))
    print "part 2:", part2(inputs)
