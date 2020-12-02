import re

rule_pattern = re.compile("^([0-9]+)-([0-9]+) (.)$")

def part1(inputs):
    valid = 0

    for line in inputs:
        raw_rule, password = line.split(": ")
        rule = rule_pattern.match(raw_rule)
        occurence = password.count(rule.group(3))
        if occurence >= int(rule.group(1)) and occurence <= int(rule.group(2)):
            valid += 1

    return valid

def part2(inputs):
    valid = 0

    for line in inputs:
        raw_rule, password = line.split(": ")
        low, high, val = rule_pattern.match(raw_rule).groups()
        count = 0

        if password[int(low) - 1] == val:
            count += 1

        if password[int(high) - 1] == val:
            count += 1

        if count == 1:
            valid += 1

    return valid


if __name__ == "__main__":
    print "part 1:", part1([line.strip() for line in open("input.txt").readlines()])
    print "part 2:", part2([line.strip() for line in open("input.txt").readlines()])
