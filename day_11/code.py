OPEN="L"
OCC="#"
FLOOR="."

def part1(inputs):
    state = inputs    

    while True:
        new_state = step(state, False, 4)
        if new_state == state:
            return sum([row.count(OCC) for row in new_state])
        else:
            state = new_state

def part2(inputs):
    state = inputs    

    while True:
        new_state = step(state, True, 5)
        if new_state == state:
            return sum([row.count(OCC) for row in new_state])
        else:
            state = new_state

def step(inputs, full, occupied_threshold):
    new_state = []

    for row in range(0, HEIGHT):
        new_state.append([])
        for col in range(0, len(inputs[row])):
            val = inputs[row][col]

            if val == FLOOR:
                new_val = FLOOR
            elif val == OPEN:
                new_val = process_empty_seat(inputs, row, col, full)
            else:
                new_val = process_occupied_seat(inputs, row, col, full, occupied_threshold)
                
            new_state[row].append(new_val)

    return new_state

def process_empty_seat(inputs, row, col, full):
    return OCC if all(map(lambda x: x == "L", find_adjacent_positions(inputs, row, col, full))) else OPEN

def process_occupied_seat(inputs, row, col, full, threshold):
    return OPEN if len([p for p in find_adjacent_positions(inputs, row, col, full) if p == OCC]) >= threshold else OCC

def find_adjacent_positions(inputs, row, col, full, debug=False):
    positions = []
    ps = {}

    left_ok = col != 0
    right_ok = col != len(inputs[row]) - 1
    up_ok = row != 0
    down_ok = row != HEIGHT - 1

    if full:
        if left_ok: positions.append(left(inputs, row, col)) #left
        if right_ok: positions.append(right(inputs, row, col)) #right
        if up_ok: positions.append(up(inputs, row, col)) #up
        if down_ok: positions.append(down(inputs, row, col)) #down
        
        if up_ok and left_ok: positions.append(up_left(inputs, row, col)) #up-left
        if up_ok and right_ok: positions.append(up_right(inputs, row, col)) #up-right

        if down_ok and left_ok: positions.append(down_left(inputs, row, col)) #down-left
        if down_ok and right_ok: positions.append(down_right(inputs, row, col)) #down-right

    else:
        if left_ok: positions.append(inputs[row][col-1]) #left
        if right_ok: positions.append(inputs[row][col+1]) #right
        if up_ok: positions.append(inputs[row-1][col]) #up
        if down_ok: positions.append(inputs[row+1][col]) #down

        if up_ok and left_ok: positions.append(inputs[row-1][col-1]) #up-left
        if down_ok and left_ok: positions.append(inputs[row+1][col-1]) #up-left
        if up_ok and right_ok: positions.append(inputs[row-1][col+1]) #up-right
        if down_ok and right_ok: positions.append(inputs[row+1][col+1]) #up

    return [p for p in positions if p != FLOOR]

def left(inputs, row, col):
    return first_seat(inputs[row][max(col-1, 0)::-1])

def right(inputs, row, col):
    return first_seat(inputs[row][col+1:len(inputs[row])])

def up(inputs, row, col):
    return first_seat([p[col] for p in inputs[max(row-1, 0)::-1]])

def down(inputs, row, col):
    return first_seat([p[col] for p in inputs[row+1:HEIGHT]])

def up_left(inputs, row, col):
    return first_seat([inputs[row-i][col-i] for i in range(1, row+1) if col-i >= 0])

def up_right(inputs, row, col):
    return first_seat([inputs[row-i][col+i] for i in range(1, row+1) if col+i < WIDTH])

def down_left(inputs, row, col):
    return first_seat([inputs[row+i][col-i] for i in range(1, HEIGHT - row) if col-i >= 0])

def down_right(inputs, row, col):
    return first_seat([inputs[row+i][col+i] for i in range(1, HEIGHT - row) if col+i < WIDTH])


def first_seat(positions):
    for p in positions:
        if p != FLOOR:
            return p

    return FLOOR


def print_state(inputs):
    print ""
    for row in inputs: print "".join(row)

if __name__ == "__main__":
    inputs = [list(line.strip()) for line in open("input.txt").readlines()]

    WIDTH = len(inputs[0])
    HEIGHT = len(inputs)

    print "part 1:", part1(inputs)
    print "part 2:", part2(inputs)
