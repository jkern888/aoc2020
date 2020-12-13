OPEN="L"
OCC="#"
FLOOR="."

def part1(inputs):
    return find_stable(inputs, False, 4)

def part2(inputs):
    return find_stable(inputs, True, 5)

def find_stable(inputs, seat_only, occupied_threshold):
    state = inputs    

    while True:
        new_state = step(state, seat_only, occupied_threshold)
        if new_state == state:
            return sum([row.count(OCC) for row in new_state])
        else:
            state = new_state

def step(inputs, seat_only, occupied_threshold):
    new_state = []

    for row in range(0, HEIGHT):
        new_state.append([])
        for col in range(0, len(inputs[row])):
            val = inputs[row][col]

            if val == FLOOR:
                new_val = FLOOR
            elif val == OPEN:
                new_val = process_empty_seat(inputs, row, col, seat_only)
            else:
                new_val = process_occupied_seat(inputs, row, col, seat_only, occupied_threshold)
                
            new_state[row].append(new_val)

    return new_state

def process_empty_seat(inputs, row, col, seat_only):
    return OCC if all(map(lambda x: x == "L", find_adjacent_positions(inputs, row, col, seat_only))) else OPEN

def process_occupied_seat(inputs, row, col, seat_only, threshold):
    return OPEN if len([p for p in find_adjacent_positions(inputs, row, col, seat_only) if p == OCC]) >= threshold else OCC

def find_adjacent_positions(inputs, row, col, seat_only, debug=False):
    positions = []

    left = col != 0
    right = col != len(inputs[row]) - 1
    up = row != 0
    down = row != HEIGHT - 1

    if left: positions.append(first_seat(inputs[row][max(col-1, 0)::-1], seat_only)) #left
    if right: positions.append(first_seat(inputs[row][col+1:len(inputs[row])], seat_only)) #right
    if up: positions.append(first_seat([p[col] for p in inputs[max(row-1, 0)::-1]], seat_only)) #up
    if down: positions.append(first_seat([p[col] for p in inputs[row+1:HEIGHT]], seat_only)) #down
    
    if up and left: positions.append(first_seat([inputs[row-i][col-i] for i in range(1, row+1) if col-i >= 0], seat_only)) #up-left
    if up and right: positions.append(first_seat([inputs[row-i][col+i] for i in range(1, row+1) if col+i < WIDTH], seat_only)) #up-right

    if down and left: positions.append(first_seat([inputs[row+i][col-i] for i in range(1, HEIGHT - row) if col-i >= 0], seat_only)) #down-left
    if down and right: positions.append(first_seat([inputs[row+i][col+i] for i in range(1, HEIGHT - row) if col+i < WIDTH], seat_only)) #down-right

    return [p for p in positions if p != FLOOR]

def first_seat(positions, seat_only):
    for p in positions:
        if p != FLOOR or not seat_only:
            return p

    return FLOOR

if __name__ == "__main__":
    inputs = [list(line.strip()) for line in open("input.txt").readlines()]

    WIDTH = len(inputs[0])
    HEIGHT = len(inputs)

    print "part 1:", part1(inputs)
    print "part 2:", part2(inputs)
