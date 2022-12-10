class Node:
    def __init__(
        self, height, id, top=None, right=None, bottom=None, left=None
    ) -> None:
        self.height = height
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.visited = False
        self.id = id

    def get_left_edge(self):
        if self.left is None:
            return self
        else:
            return self.left.get_left_edge()

    def is_edge(self):
        return (
            self.top is None
            or self.right is None
            or self.bottom is None
            or self.left is None
        )


def parse(input_file):
    return [map(int, e) for e in map(list, open(input_file, "r").read().splitlines())]


def build_map(lines):
    curr_node = None
    tree_map = [[] for _ in lines]
    id = 0
    for i, line in enumerate(lines):
        for j, e in enumerate(line):
            if curr_node is None:
                curr_node = Node(e, id)
            else:
                if j == 0:
                    curr_node = curr_node.get_left_edge()
                    new_node = Node(e, id, top=curr_node)
                    curr_node.bottom = new_node
                    curr_node = new_node
                else:
                    if i > 0:
                        new_node = Node(e, id, left=curr_node, top=curr_node.top.right)
                        curr_node.right = new_node
                        curr_node.top.right.bottom = new_node
                        curr_node = new_node
                    else:
                        new_node = Node(e, id, left=curr_node)
                        curr_node.right = new_node
                        curr_node = new_node

            tree_map[i].append(curr_node)
            id += 1

    return tree_map


def part_one(input_file):
    tree_map = build_map(parse(input_file))
    all_visited = set()

    for line in tree_map:
        for e in line:
            if not e.is_edge():
                continue

            max_h = e.height
            all_visited.add(e.id)

            if e.top is None:
                curr = e.bottom
                while curr is not None:
                    if curr.height > max_h:
                        max_h = curr.height
                        all_visited.add(curr.id)
                    curr = curr.bottom

            if e.right is None:
                curr = e.left
                while curr is not None:
                    if curr.height > max_h:
                        max_h = curr.height
                        all_visited.add(curr.id)
                    curr = curr.left

            if e.bottom is None:
                curr = e.top
                while curr is not None:
                    if curr.height > max_h:
                        max_h = curr.height
                        all_visited.add(curr.id)
                    curr = curr.top

            if e.left is None:
                curr = e.right
                while curr is not None:
                    if curr.height > max_h:
                        max_h = curr.height
                        all_visited.add(curr.id)
                    curr = curr.right

    return len(all_visited)


def part_two(input_file):
    tree_map = build_map(parse(input_file))
    all_visited = set()

    max_score = 0

    for line in tree_map:
        for e in line:
            top, right, bottom, left = 0, 0, 0, 0

            curr = e.bottom
            while curr is not None:
                if curr.height < e.height:
                    bottom += 1
                if curr.height >= e.height:
                    bottom += 1
                    break
                curr = curr.bottom

            curr = e.left
            while curr is not None:
                if curr.height < e.height:
                    left += 1
                if curr.height >= e.height:
                    left += 1
                    break
                curr = curr.left

            curr = e.top
            while curr is not None:
                if curr.height < e.height:
                    top += 1
                if curr.height >= e.height:
                    top += 1
                    break
                curr = curr.top

            curr = e.right
            while curr is not None:
                if curr.height < e.height:
                    right += 1
                if curr.height >= e.height:
                    right += 1
                    break
                curr = curr.right

            score = top * right * bottom * left
            if score > max_score:
                max_score = score

    return max_score


if __name__ == "__main__":
    input_file = "example_input.txt"
    input_file = "input.txt"

    print("Part one: ", part_one(input_file))
    print("Part two: ", part_two(input_file))
