import re
import time

class TicketReader:
    def __init__(self, inputs):
        self.valid_values = [0] * 1000
        self.other_tickets = []
        self.rules = {}
        
        mode = None
        for line in inputs:
            if line == "your ticket:":
                mode = 1
                continue
            elif line == "nearby tickets:":
                mode = 2
                continue

            if not mode:
                name, val = line.split(":")
                rule_ranges = re.findall("([0-9]+)-([0-9]+)", val)
                self.rules[name] = (int(rule_ranges[0][0]), int(rule_ranges[0][1]), int(rule_ranges[1][0]), int(rule_ranges[1][1]))
                for start, end in rule_ranges:
                    for i in range(int(start), int(end)+1):
                        self.valid_values[i] = 1
            elif mode == 1:
                self.my_ticket = [int(val) for val in line.split(",")]
            else:
                self.other_tickets.append([int(val) for val in line.split(",")])


def part1(reader):
    total = 0
    for ticket in reader.other_tickets:
        for num in ticket:
            if reader.valid_values[num] == 0:
                total += num
    return total   

def part2(reader):
    rule_guesses = [{rule: reader.rules[rule] for rule in reader.rules.keys()} for _ in range(0, len(reader.my_ticket))]

    for ticket in reader.other_tickets:
        if invalid_ticket(ticket, reader):
            continue

        for i, num in enumerate(ticket):
            for rule_name, rule_guess in rule_guesses[i].items():
                check = rule_guess[0] <= num <= rule_guess[1] or rule_guess[2] <= num <= rule_guess[3]
                if not check:
                    del rule_guesses[i][rule_name]
    
    field_guesses = sorted(enumerate(rule_guesses), key=lambda item: len(item[1]))
    fields = [None] * len(field_guesses)

    for field, choices in field_guesses:
        for rule in choices.keys():
            if rule not in fields:
                fields[field] = rule
                break

    product = 1
    for i, field in enumerate(fields):
        if field.startswith("departure"):
            product *= reader.my_ticket[i]

    return product

def invalid_ticket(ticket, reader):
    for num in ticket:
        if reader.valid_values[num] == 0:
            return True
    return False

if __name__ == "__main__":
    inputs = [line.strip() for line in open("input.txt").readlines() if line.strip()]
    reader = TicketReader(inputs)

    print "part 1:", part1(reader)
    print "part 2:", part2(reader)
