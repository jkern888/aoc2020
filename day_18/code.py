def part1(inputs):
    return sum(map(lambda x: x[1], map(calc_expr_no_order, inputs)))

def part2(inputs):
    return sum(map(lambda x: x[1], map(calc_expr_order, inputs)))

def calc_expr_no_order(expr):
    if show: 
        print expr, "=", calc_expr(expr, False)[1]
    return calc_expr(expr, False)

def calc_expr_order(expr):
    if show:
        print expr, "=", calc_expr(expr, True)[1]
    return calc_expr(expr, True)

def calc_expr(expr, order=False, indent=" ", fallthrough=False):
    i = 0
    stack = []
    while i < len(expr):
        val = expr[i]

        if debug:
            print indent, i, val, ": ", "".join([str(v) for v in expr]), stack

        if val == "(":
            jump, val = calc_expr(expr[i+1:], order, indent + " ", fallthrough)
            i += jump

            if fallthrough:
                i -= 1
            else:
                i += 1

        elif val == ")":
            break

        stack.append(val)

        if len(stack) == 3:
            if stack[1] == "*" and order:
                jump, stack[2] = calc_expr([stack[2]] + expr[i+1:], order, indent + " ", True)
                i += jump 
            stack = [calc_stack(stack)]

        i += 1
    return i, stack[0]

def calc_stack(stack):
    left, opr, right = int(stack[0]), stack[1], int(stack[2])

    if opr == "+":
        res = left + right
    else:
        res = left * right

    if res == 216:
        import pdb;pdb.set_trace()

    if debug:
        print stack, "=", res

    return res


if __name__ == "__main__":
    inputs = [line.strip().replace("(", "( ").replace(")", " )").split(" ") for line in open("sample.txt").readlines()]
    debug = True
    show = True
    print calc_expr(['(', '(', '2', '+', '4', '*', '9', ')', '*', '(', '6', '+', '9', '*', '8', '+', '6', ')', '+', '6', ')', '+', '2', '+', '4', '*', '2'], True)
    #print calc_expr(['1', '+', '(', '2', '*', '3', ')', '+', '(', '4', '*', '(', '5', '+', '6', ')', ')'], False)
    #print
    #print calc_expr(['1', '+', '(', '2', '*', '3', ')', '+', '(', '4', '*', '(', '5', '+', '6', ')', ')'], True)
    #print
    #print calc_expr(list("(2*2)+1"), True)
    #print calc_expr(list("(2*2+3"), True)
    #print "part 1:", part1(inputs)
    #print "part 2:", part2(inputs)
