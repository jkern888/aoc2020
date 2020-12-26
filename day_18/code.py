def part1(inputs):
    return sum(map(lambda expr: eval(expr, ["+*"]), inputs))

def part2(inputs):
    return sum(map(lambda expr: eval(expr, ["+", "*"]), inputs))

def eval(expr, opers):
    parsed = parse_expr(expr)[1]
    return eval_expr(parsed, opers)

def parse_expr(expr):
    rewrite = []
    i = 0

    while i < len(expr):
        read, val = read_next(expr, i)
        i += read

        if val == ")":
            break

        rewrite.append(val)
    return i, rewrite

def read_next(expr, i):
    if expr[i] == "(":
        read, val = parse_expr(expr[i+1:])
        return read + 1, val

    return 1, expr[i]

def eval_expr(parsed, opers):
    for i, val in enumerate(parsed):
        if type(val) is list:
            parsed[i] = eval_expr(val, opers)
 
    for oper_set in opers:
        i = 0
        while i < len(parsed) and len(parsed) > 1:
            val = parsed[i]
            if type(val) is str and val in oper_set:
                left, oper, right = parsed[i-1:i+2]
                val = calc(left, right, oper)                
                reduced = parsed[0:i-1] + [val]

                if i + 2 < len(parsed):
                    reduced.extend(parsed[i+2:])
                
                parsed = reduced
                i -= 2
            else :
                i += 1
    return parsed[0]

def calc(left, right, oper):
    left, right = int(left), int(right)
    return left + right if oper == "+" else left * right


if __name__ == "__main__":
    inputs = [line.strip().replace("(", "( ").replace(")", " )").split(" ") for line in open("input.txt").readlines()]
    print "part 1:", part1(inputs)
    print "part 2:", part2(inputs)
