import re

def part1(deps):
    rev = deps["shiny gold"]["rev"]
    parents = []    

    while rev:
        color = rev.pop()
        parents.append(color)

        if "rev" in deps[color]:
            rev.extend(deps[color]["rev"])

    return len(set(parents))

def part2(deps):
    return count_deps(deps, deps["shiny gold"]["deps"])

def count_deps(deps, color_deps):
    if not color_deps:
        return 0

    total = 0
    for count, color in color_deps:
        children = count_deps(deps, deps[color]["deps"])
        total += count + (count * children)

    return total

def build_deps(inputs):
    deps = {}

    for line in inputs:
        match = re.match("^(.*) bags contain (.*)$", line)
        color = match.group(1)

        dep_matches = re.findall("([0-9]+) (.*?) (bag|bags)[,.]", match.group(2))
        color_deps = [(int(dep_match[0]), dep_match[1]) for dep_match in dep_matches ] if dep_matches else []
        deps.setdefault(color, dict())["deps"] = color_deps

        for dep in color_deps:
            deps.setdefault(dep[1], dict()).setdefault("rev", list()).append(color)        

    return deps

if __name__ == "__main__":
    deps = build_deps([line.strip() for line in open("input.txt").readlines()])
    print "part 1:", part1(deps)
    print "part 2:", part2(deps)
