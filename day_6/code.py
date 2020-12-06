def part1(groups):
    return sum(map(lambda x: x[0], map(count, groups)))

def part2(groups):
    return sum(map(lambda x: x[1], map(count, groups)))

def count(group):
    unions, inters = None, None

    for person in group.split("\n"):
        unions = unions.union(set(list(person))) if unions is not None else set(list(person))
        inters = inters.intersection(set(list(person))) if inters is not None else set(list(person))

    return len(unions), len(inters)

if __name__ == "__main__":
    groups = open("input.txt").read().split("\n\n")

    print "part 1:", part1(groups)
    print "part 2:", part2(groups)
