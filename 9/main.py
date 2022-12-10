import numpy as np


class Node:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def move_to(self, node):
        if self.x != node.x and self.y != node.y:
            if abs(self.y - node.y) > 1 or abs(self.x - node.x) > 1:
                self.x += -1 * (abs(self.x - node.x) / (self.x - node.x))
                self.y += -1 * (abs(self.y - node.y) / (self.y - node.y))
        elif self.x == node.x:
            self.move_y(node)
        elif self.y == node.y:
            self.move_x(node)

    def move_x(self, node):
        if abs(self.x - node.x) > 1:
            self.x += -1 * (abs(self.x - node.x) / (self.x - node.x))

    def move_y(self, node):
        if abs(self.y - node.y) > 1:
            self.y += -1 * (abs(self.y - node.y) / (self.y - node.y))


def parse(input_file):
    return map(
        lambda x: [x[0], int(x[1])],
        map(str.split, open(input_file, "r").read().splitlines()),
    )


def simulate(lines, n_segments):
    rope = [Node() for _ in range(n_segments)]
    tail_positions = set([(0, 0)])
    for direction, steps in lines:
        if direction == "U":
            for _ in range(steps):
                rope[0].y += 1
                for prev_segment, segment in zip(rope, rope[1:]):
                    segment.move_to(prev_segment)
                tail_positions.add((rope[-1].x, rope[-1].y))

        elif direction == "R":
            for _ in range(steps):
                rope[0].x += 1
                for prev_segment, segment in zip(rope, rope[1:]):
                    segment.move_to(prev_segment)
                tail_positions.add((rope[-1].x, rope[-1].y))

        elif direction == "D":
            for _ in range(steps):
                rope[0].y -= 1
                for prev_segment, segment in zip(rope, rope[1:]):
                    segment.move_to(prev_segment)
                tail_positions.add((rope[-1].x, rope[-1].y))

        elif direction == "L":
            for _ in range(steps):
                rope[0].x -= 1
                for prev_segment, segment in zip(rope, rope[1:]):
                    segment.move_to(prev_segment)
                tail_positions.add((rope[-1].x, rope[-1].y))

    return len(tail_positions)


def part_one(input_file):
    return simulate(parse(input_file), 2)


def part_two(input_file):
    return simulate(parse(input_file), 10)


if __name__ == "__main__":
    # input_file = "example_input.txt"
    input_file = "input.txt"

    print("Part one: ", part_one(input_file))
    print("Part two: ", part_two(input_file))
