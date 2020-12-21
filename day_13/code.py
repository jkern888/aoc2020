def part1(start_tick, buses):
    buses = [int(val) for val in buses.split(",") if val != "x"]
    next_leave = None
    for bus in buses:
        bus_leave = bus - start_tick % bus
        if next_leave is None or bus_leave < next_leave[0]:
            next_leave = (bus_leave, bus)

    return next_leave[0] * next_leave[1] 

def part2(buses):
    time, step = 0, 1
    bus_schedule = [(i, int(bus)) for i, bus in enumerate(buses.split(',')) if bus != 'x']

    for minute, bus_id in bus_schedule:
        print time, step, minute, bus_id
        while (time + minute) % bus_id != 0:
            time += step
        step *= bus_id
    return time

if __name__ == "__main__":
    inputs = [line for line in open("input.txt").readlines()]
    start_tick = int(inputs[0])

    print "part 1:", part1(start_tick, inputs[1])
    print "part 2:", part2(inputs[1])
