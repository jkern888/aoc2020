def part1(groups):
    return sum(map(lambda x: x[0], map(count, groups)))

def part2(groups):
    return sum(map(lambda x: x[1], map(count, groups)))

def count(group):
    sets = [set(list(person)) for person in group.split("\n")]
    return len(set.union(*sets)), len(set.intersection(*sets))

if __name__ == "__main__":
    groups = open("input.txt").read().split("\n\n")

    print "part 1:", part1(groups)
    print "part 2:", part2(groups)
