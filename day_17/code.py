steps = range(-1, 2)

def part1(inputs):
    state = gen_state(1, 30, 30, 30)

    for i, line in enumerate(inputs):
        for j, val in enumerate(line):
            state[0][15][15+i][15+j] = val

    for _ in range(0, 6):
        new_state = gen_state(1, 30, 30, 30)
        active = 0

        for i in range(1, 29):
            for j in range(1, 29):
                for k in range(1, 29):
                    new_val = incr_val(state, 0, i, j, k)
                    new_state[0][i][j][k] = new_val
                    if new_val == "#":
                        active += 1

        state = new_state
    return active

def part2(inputs):
    state = gen_state(25, 25, 25, 25)

    for i, line in enumerate(inputs):
        for j, val in enumerate(line):
            state[10][10][10+i][10+j] = val

    for _ in range(0, 6):
        new_state = gen_state(25, 25, 25, 25)
        active = 0
        for i in range(1, 24):
            for j in range(1, 24):
                for k in range(1, 24):
                    for l in range(1,24):
                        new_val = incr_val(state, i, j, k, l)
                        new_state[i][j][k][l] = new_val
                        if new_val == "#":
                            active += 1

        state = new_state
    return active

def incr_val(state, a, z, y, x):
    active = 0
    a_steps = steps if a != 0 else [0]

    for i in a_steps:
        for j in steps:
            for k in steps:
                for l in steps:
                    if i == 0 and j == 0 and k == 0 and l == 0:
                        continue

                    if state[a+i][z+j][y+k][x+l] == "#":
                        active += 1
    
    if (state[a][z][y][x] == "." and active == 3) or (state[a][z][y][x] == "#" and 2 <= active <= 3):
        return "#"

    return "."

def gen_state(a, z, y, x):
    return [[[["." for _ in range(0, x)] for _ in range(0, y)] for _ in range(0, z)] for _ in range(0, a)]

if __name__ == "__main__":
    inputs = [line.strip() for line in open("input.txt").readlines()]

    print "part 1:", part1(inputs)
    print "part 2:", part2(inputs)
