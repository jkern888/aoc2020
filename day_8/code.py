def run(inputs, swap_pos):
    accumulator, i, swap_count = 0, 0, 0

    while i < len(inputs):
        cmd = inputs[i]
        
        if cmd is None:
            return accumulator, False

        cmd, val = cmd.split(" ")
        inputs[i] = None

        if cmd == "nop" or cmd == "jmp":
            if swap_count == swap_pos:
                cmd = "jmp" if cmd == "nop" else "nop"
            swap_count += 1

        if cmd == "acc":
            accumulator += int(val)
            i += 1
        elif cmd == "nop":
            i += 1
        elif cmd == "jmp":
            i += int(val)

    return accumulator, True 

def part1(inputs):
    return run(inputs[:], -1)[0]

def part2(inputs):
    swap = 0
    while swap < len(inputs):
        output, success = run(inputs[:], swap)

        if not success:
            swap += 1
        else:
            return output

if __name__ == "__main__":
    inputs = open("input.txt").readlines()

    print "part 1:", part1(inputs)
    print "part 2:", part2(inputs)
