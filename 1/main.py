def parse(input_file: str):
    return [
        sum(map(int, e.split("\n"))) for e in open(input_file, "r").read().split("\n\n")
    ]


def part_one(input_file: str):
    return max(parse(input_file))


def part_two(input_file: str):
    return sum(sorted(parse(input_file), reverse=True)[:3])


if __name__ == "__main__":
    print("Part one: ", part_one("input.txt"))
    print("Part two: ", part_two("input.txt"))
