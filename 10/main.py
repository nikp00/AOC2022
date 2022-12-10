def parse(input_file):
    return map(str.split, open(input_file, "r").read().splitlines())


def part_one(input_file):
    x = 1
    cycles = 0
    ir_cycles = 0
    signal_sum = 0
    for cmd in parse(input_file):
        if cmd[0] == "noop":
            cycles += 1
            if cycles in (20, 60, 100, 140, 180, 220):
                signal_sum += cycles * x
        elif cmd[0] == "addx":
            ir_cycles = 2
            while ir_cycles:
                if ir_cycles > 0:
                    cycles += 1
                    ir_cycles -= 1

                if cycles in (20, 60, 100, 140, 180, 220):
                    signal_sum += cycles * x

                if ir_cycles == 0:
                    x += int(cmd[1])
    return signal_sum


def draw_pixel(cycles, x):
    if cycles % 40 in (x, x + 1, x + 2):
        print("#", end="")
    else:
        print(".", end="")

    if cycles % 40 == 0:
        print()


def part_two(input_file):
    x = 1
    cycles = 0
    ir_cycles = 0
    signal_sum = 0
    for cmd in parse(input_file):
        if cmd[0] == "noop":
            cycles += 1
            draw_pixel(cycles, x)
        elif cmd[0] == "addx":
            ir_cycles = 2
            while ir_cycles:
                if ir_cycles > 0:
                    cycles += 1
                    ir_cycles -= 1

                draw_pixel(cycles, x)

                if ir_cycles == 0:
                    x += int(cmd[1])
    return signal_sum


if __name__ == "__main__":
    input_file = "example_input.txt"
    input_file = "input.txt"

    print("Part one: ", part_one(input_file))
    print("Part two: ")
    part_two(input_file)
