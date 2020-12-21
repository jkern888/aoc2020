def part1(inputs):
    inputs = sorted(inputs)

    for i in range(0, len(inputs)):
        if inputs[i] >= 2020: 
            break

        for j in range(len(inputs) -1, i, -1):
            if inputs[i] + inputs[j] == 2020:
                return inputs[i], inputs[j], inputs[i] * inputs[j]
            elif inputs[i] + inputs[j] < 2020:
                break

    return []

def part2(inputs):
    inputs = sorted(inputs)

    for i in range(0, len(inputs)):
        a = inputs[i]
        if a >= 2020: 
            break

        for j in range(i+1, len(inputs)):
            b = inputs[j]

            if a + b >= 2020:
                break

            for k in range(j+1, len(inputs)):
                c = inputs[k]

                if a + b + c == 2020:
                    return a,b,c, a * b * c
                elif a + b + c > 2020:
                    break

    return []



if __name__ == "__main__":
    print "part 1 answer:", part1([int(val.strip()) for val in open("input_1.txt").readlines()])
    print "part 2 answer:", part2([int(val.strip()) for val in open("input_1.txt").readlines()])
