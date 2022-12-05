def parse(input_file):
    stacks = []
    moves = []
    parse_stack = True
    for line in open(input_file).read().splitlines():
        if parse_stack:
            for i, e in enumerate(line.replace("    ", " --- ").split()):
                if len(stacks) <= i:
                    stacks.append([])
                if "[" in e:
                    stacks[i].insert(0, e[1])

            line = line.split()
            if len(line) > 0 and line[0].isdigit():
                max_stack = int(line[-1].replace("-", ""))
                stacks = stacks[:max_stack]
                parse_stack = False

        elif not parse_stack and len(line) > 0:
            move = list(map(lambda x: int(x), [e for e in line.split() if e.isdigit()]))
            moves.append([move[0], move[1] - 1, move[2] - 1])

    return stacks, moves


def part_one(input_file):
    stacks, moves = parse(input_file)

    for n, f, t in moves:
        for _ in range(n):
            stacks[t].append(stacks[f].pop())

    return "".join(e[-1] for e in stacks)


def part_two(input_file):
    stacks, moves = parse(input_file)

    for n, f, t in moves:
        pos = len(stacks[t])
        for _ in range(n):
            stacks[t].insert(pos, stacks[f].pop())

    return "".join(e[-1] for e in stacks)


if __name__ == "__main__":
    # input_file = "example_input.txt"
    input_file = "input.txt"

    print("Part one: ", part_one(input_file))
    print("Part two: ", part_two(input_file))
