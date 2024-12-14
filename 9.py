from tqdm import tqdm


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

    def find_free_arr():
        nonlocal free_arr

        free_arr = [0] * len(diskmap)
        for idx in range(len(diskmap)):
            prev = free_arr[idx - 1] if idx > 0 else 0
            free_arr[idx] = 0 if diskmap[idx] is not None else 1 + prev

    find_free_arr()

    for file_id in tqdm(sorted(file_map.keys(), reverse=True)):
        start_loc, length = file_map[file_id]

        for i in range(start_loc):
            if free_arr[i] >= length:
                free_start = i - length + 1
                diskmap[free_start:free_start+length] = [file_id]*length
                diskmap[start_loc:start_loc+length] = [None]*length
                find_free_arr()
                break

    print(sum([diskmap[i] * i for i in range(len(diskmap)) if diskmap[i] is not None]))
