def part1(inputs):
    mem_bank = {}

    for cmd in inputs:
        if cmd[0] == "mask":
            mask = cmd[1]
            continue

        _, mem, val = cmd

        res = ["0"] * 36

        for i in range(0, 36):
            res[i] = val[i] if mask[i] == "X" else mask[i]

        mem_bank[mem] = int("".join(res), 2)

    return sum(mem_bank.values())
    

def part2(inputs):
    mem_bank = {}

    for cmd in inputs:
        if cmd[0] == "mask":
            mask = cmd[1]
            continue

        _, mem, val = cmd

        res = ["0"] * 36
        mem = bin(mem)[2:].rjust(36, "0")

        for i in range(0, 36):
            res[i] = mem[i] if mask[i] == "0" else mask[i]

        mem_bank.update({int("".join(addr), 2): int(val, 2) for addr in find_fuzzy_addrs(res)})

    return sum(mem_bank.values())
 
def find_fuzzy_addrs(fuzz):
    addrs = []

    if "X" not in fuzz:
        return [fuzz]

    for i in range(0, len(fuzz)):
        if fuzz[i] == "X":
            base = fuzz[0:i]
            subs = find_fuzzy_addrs(fuzz[i+1:]) 
            for val in ["0", "1"]:
                for sub in subs:
                    addrs.append(base + [val] + sub)
            return addrs

def tokenize(line):
    if line.startswith("mask"):
        return line.split("=")
    else: 
        mem, val = line.split("=")
        return ("mem", int(mem.replace("]", "").split("[")[1]), bin(int(val))[2:].rjust(36, "0"))

if __name__ == "__main__":
    inputs = [tokenize(line.replace(" ", "").strip()) for line in open("input.txt").readlines()]

    print "part 1:", part1(inputs)
    print "part 2:", part2(inputs)
