def parse(input_file):
    return [
        list(
            map(
                lambda x: ord(x) - ord("A") if ord(x) <= ord("C") else ord(x) - 88,
                e.split(),
            )
        )
        for e in open(input_file).read().splitlines()
    ]


def sum_points(moves):
    return sum(
        [
            ((e1 + (e1 + e2)) % 3 - (e2 + (e1 + e2)) % 3 - 1) * -1 * 3 + e2 + 1
            for e1, e2 in moves
        ]
    )


def part_one(input_file):
    return sum_points(parse(input_file))


def part_two(input_file):
    return sum_points([e1, (e1 + o - 1) % 3] for e1, o in parse(input_file))


if __name__ == "__main__":
    # input_file = "example_input.txt"
    # input_file = "example_input2.txt"
    input_file = "input.txt"

    print("Part one: ", part_one(input_file))
    print("Part two: ", part_two(input_file))
