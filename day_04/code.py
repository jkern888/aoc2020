import re

valid_set = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def parse_passports(inputs):
    passports = []
    passport = {}

    for line in inputs:
        if line == "":
            passports.append(passport)
            passport = {}
            continue

        for pair in line.split(" "):
            key, val = pair.split(":")
            if key in valid_set:
                passport[key] = val

    return passports

def is_valid(passport):
    try:
        return (1920 <= int(passport["byr"]) <= 2002 
            and 2010 <= int(passport["iyr"]) <= 2020
            and 2020 <= int(passport["eyr"]) <= 2030
            and re.match("^#[0-9a-f]{6}$", passport["hcl"])
            and re.match("^[0-9]{9}$", passport["pid"])
            and passport["ecl"] in eye_colors
            and height_is_valid(passport["hgt"]))
    except:
        return False

def height_is_valid(hgt):
    match = re.match("^([0-9]+)(cm|in)$", hgt)

    if not match:
        return False
    elif match.group(2) == "cm":
        return 150 <= int(match.group(1)) <= 193
    else:
        return 59 <= int(match.group(1)) <= 76
        
        
def part1(passports):
    return sum(map(lambda passport: set(passport.keys()) == valid_set, passports))

def part2(inputs):
    return sum(map(lambda passport: bool(is_valid(passport)), passports))

if __name__ == "__main__":
    inputs = [line.strip() for line in open("input.txt").readlines()]
    passports = parse_passports(inputs)

    print "part 1:", part1(passports)
    print "part 2:", part2(inputs)
