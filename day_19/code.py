import re

def part1(rule, messages):
    total = 0
    rule = re.compile("^" + rule.pattern + "$")
    print(rule)
    for msg in messages:
        if rule.match(msg):
            total+=1

    return total

def part2(inputs):
    pass

def parse_inputs(inputs):
    rules = []
    messages = []

    read_rules = True

    for line in inputs:
        if not line:
            read_rules = False
            continue

        if read_rules:
            rules.append(line)
        else:
            messages.append(line)

    return build_rules(rules), messages

def build_rules(input_rules):
    rules = {int(r.split(":")[0]): r.split(": ")[1].replace('"', '').split(" ") for r in input_rules}
    
    for i, raw_rule in rules.items():
        rules[i] = build_rule(rules, raw_rule)
    return rules
            
def build_rule(rules, raw_rule):
    if type(raw_rule) is not list:
        return raw_rule

    rule = []
    add_close = False
    for val in raw_rule:
        if val.isdigit():
            key = int(val)
            rules[key] = build_rule(rules, rules[key])
            rule.append(rules[key].pattern)
        elif val == "|":
            rule.insert(0, "(")
            rule.append("|")
            add_close = True
        else:
            rule.append(val)
            
    if add_close:
        rule.append(")")

    return re.compile("".join(rule))

if __name__ == "__main__":
    inputs = [line.strip() for line in open("input.txt").readlines()]

    rules, messages = parse_inputs(inputs)

    print("part 1:", part1(rules[0], messages))
    print("part 2:", part2(inputs))
