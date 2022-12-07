def parse(input_file):
    return open(input_file, "r").read().strip()


def part_one(input_file):
    data = parse(input_file)
    for i in range(1, len(data)):
        if len(set(data[i : i + 4])) == 4:
            return i + 4


def part_two(input_file):
    data = parse(input_file)
    for i in range(1, len(data)):
        if len(set(data[i : i + 14])) == 14:
            return i + 14


if __name__ == "__main__":
    input_file = "example_input.txt"
    input_file = "input.txt"

    print("Part one: ", part_one(input_file))
    print("Part two: ", part_two(input_file))
