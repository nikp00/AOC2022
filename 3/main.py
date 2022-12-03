def convert(e):
    return ord(e) - ord("A") + 25 + 2 if ord(e) <= ord("Z") else ord(e) - ord("a") + 1


def parse(input_file):
    return [
        list(
            map(
                convert,
                e,
            )
        )
        for e in open(input_file).read().splitlines()
    ]


def part_one(input_file):
    return sum(
        sum(set(e[: len(e) // 2]) & set(e[len(e) // 2 :])) for e in parse(input_file)
    )


def part_two(input_file):
    data = parse(input_file)
    return sum(
        sum(set(e1) & set(e2) & set(e3))
        for e1, e2, e3 in zip(data[0::3], data[1::3], data[2::3])
    )


if __name__ == "__main__":
    # input_file = "example_input.txt"
    input_file = "input.txt"

    print("Part one: ", part_one(input_file))
    print("Part two: ", part_two(input_file))
