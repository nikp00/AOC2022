def parse(input_file):
    return [
        [list(map(int, k.split("-"))) for k in e.split(",")]
        for e in open(input_file).read().splitlines()
    ]


def part_one(input_file):
    count = 0
    for e1, e2 in parse(input_file):
        s1 = set(range(e1[0], e1[1] + 1))
        s2 = set(range(e2[0], e2[1] + 1))

        if len(s1 - s2) == 0 or len(s2 - s1) == 0:
            count += 1

    return count


def part_two(input_file):
    count = 0
    for e1, e2 in parse(input_file):
        s1 = set(range(e1[0], e1[1] + 1))
        s2 = set(range(e2[0], e2[1] + 1))

        if len(s1 - s2) != len(s1) or len(s2 - s1) != len(s2):
            count += 1

    return count


if __name__ == "__main__":
    # input_file = "example_input.txt"
    input_file = "input.txt"

    print("Part one: ", part_one(input_file))
    print("Part two: ", part_two(input_file))
