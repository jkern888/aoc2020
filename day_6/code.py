def part1(groups):
    return sum(map(count_union, groups))

def part2(groups):
    return sum(map(count_intersection, groups))

def count_union(group):
    return count(group, True)

def count_intersection(group):
    return count(group, False)

def count(group, union):
    answers = None

    for person in group.split("\n"):
        if union:
            answers = answers.union(set(list(person))) if answers is not None else set(list(person))
        else:
            answers = answers.intersection(set(list(person))) if answers is not None else set(list(person))

    return len(answers)

if __name__ == "__main__":
    groups = open("input.txt").read().split("\n\n")

    print "part 1:", part1(groups)
    print "part 2:", part2(groups)
