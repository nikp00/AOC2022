class Node:
    def __init__(self, name, is_dir, parent=None, size=0) -> None:
        self.is_dir = is_dir
        self.size = size
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.update_size(child.size)
        self.children.append(child)

    def update_size(self, size):
        self.size += size

        if self.parent is not None:
            self.parent.update_size(size)

    def __str__(self) -> str:
        return f"{'dir' if self.is_dir else self.size}   {self.name}"


def parse(input_file):
    return map(str.split, open(input_file, "r").read().splitlines())


def build_tree(lines):
    tree_top = Node(None, True)
    tree_curr = tree_top
    for line in parse(input_file):
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    tree_curr = tree_curr.parent
                else:
                    new_node = Node(line[2], True, parent=tree_curr)
                    tree_curr.add_child(new_node)
                    tree_curr = new_node
        elif line[0] != "dir":
            size, file = line
            tree_curr.add_child(Node(file, False, tree_curr, int(size)))

    return tree_top


def part_one(input_file):
    tree_top = build_tree(parse(input_file))
    dir_sum = 0
    stack = [tree_top]
    while len(stack) > 0:
        curr = stack.pop()
        if curr.is_dir and curr.size < 100000:
            dir_sum += curr.size

        stack.extend(curr.children)
    return dir_sum


def part_two(input_file):
    TOTAL_SPACE = 70000000
    SPACE_NEEDED = 30000000

    tree_top = build_tree(parse(input_file))
    stack = [tree_top]
    candidates = []
    current_free_space = TOTAL_SPACE - tree_top.size

    while len(stack) > 0:
        curr = stack.pop()
        if curr.is_dir and curr.size >= (SPACE_NEEDED - current_free_space):
            candidates.append(curr)
        stack.extend(curr.children)
    return min(candidates, key=lambda x: x.size).size


if __name__ == "__main__":
    input_file = "example_input.txt"
    input_file = "input.txt"

    print("Part one: ", part_one(input_file))
    print("Part two: ", part_two(input_file))
