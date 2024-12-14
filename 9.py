

def part_1():
    puzzle_input = open('inputs/9-1.txt', 'r').read()
    lengths = [int(x) for x in puzzle_input[::2]]
    free_spaces = [int(x) for x in puzzle_input[1::2]]
    diskmap = []

    def first_free(l: int) -> int | None:
        for i in range(l, len(diskmap)):
            if diskmap[i] is None:
                return i
        return None

    def last_taken(r: int) -> int | None:
        for i in range(r, -1, -1):
            if diskmap[i] is not None:
                return i
        return None

    for i in range(len(lengths)):
        diskmap += [i] * lengths[i]
        if i < len(free_spaces):
            diskmap += [None] * free_spaces[i]

    lhs = first_free(0)
    rhs = last_taken(len(diskmap) - 1)

    while lhs < rhs:
        diskmap[lhs], diskmap[rhs] = diskmap[rhs], diskmap[lhs]
        lhs = first_free(lhs)
        rhs = last_taken(rhs)

        if lhs is None or rhs is None:
            break

    diskmap = list(filter(lambda x: x is not None, diskmap))
    print(sum([diskmap[i] * i for i in range(len(diskmap))]))


def part_2():
    puzzle_input = open('inputs/9-2.txt', 'r').read()
    lengths = [int(x) for x in puzzle_input[::2]]
    free_spaces = [int(x) for x in puzzle_input[1::2]]
    diskmap = []
    file_map = {}

    for i in range(len(lengths)):
        file_map[i] = (len(diskmap), lengths[i])
        diskmap += [i] * lengths[i]
        if i < len(free_spaces):
            diskmap += [None] * free_spaces[i]

    free_arr = [0] * len(diskmap)

    for i in range(0, len(diskmap)):
        prev = free_arr[i - 1] if i > 0 else 0
        free_arr[i] = 0 if diskmap[i] is None else 1 + prev

    for i in reversed(file_map.keys()):
        pass

    print(free_arr)

if __name__ == "__main__":
    part_2()
