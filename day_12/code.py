
def part1(inputs):
    directions = ["E", "S", "W", "N"]
    ship = [0,0]
    facing = 0

    for cmd, val in inputs:
        if cmd == "F":
            cmd = directions[facing]

        if cmd == "E":
            ship[0] += val
        elif cmd == "W":
            ship[0] -= val
        elif cmd == "N":
            ship[1] += val
        elif cmd == "S":
            ship[1] -= val
        elif cmd == "L":
            incr = val/90
            facing = (facing - incr) % 4
        elif cmd == "R":
            incr = val/90
            facing = (facing + incr) % 4

    return abs(ship[0]) + abs(ship[1])

def part2(inputs):
    ship = [0,0]
    waypoint = [10,1]

    for cmd, val in inputs:
        if cmd == "F":
            ship[0] += waypoint[0] * val
            ship[1] += waypoint[1] * val
        elif cmd == "E":
            waypoint[0] += val
        elif cmd == "W":
            waypoint[0] -= val
        elif cmd == "N":
            waypoint[1] += val
        elif cmd == "S":
            waypoint[1] -= val
        elif cmd == "L":
            cmd, val = "R", 360-val

        if cmd == "R":
            incr = val/90
            for i in range(0, incr):
                waypoint = [waypoint[1], -waypoint[0]]

    return abs(ship[0]) + abs(ship[1])

if __name__ == "__main__":
    inputs = [(line[0], int(line[1:])) for line in open("input.txt").readlines()]

    print "part 1:", part1(inputs)
    print "part 2:", part2(inputs)
