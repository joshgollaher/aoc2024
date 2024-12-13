

def part_1():
    puzzle_in = open('inputs/2-1.txt', 'r').read()
    levels = list(map(lambda ln: list(map(lambda x: int(x), ln.split())), puzzle_in.split('\n')))

    safe = 0
    for level in levels:
        dirs = list(map(lambda v: 1 if v > 0 else 0, [level[x] - level[x - 1] for x in range(1, len(level))]))

        # Going one way.
        if dirs.count(dirs[0]) != len(dirs):
            continue

        # Between 1 and 3.
        if not all(map(lambda v: True if 1 <= v <= 3 else False, [abs(level[x] - level[x - 1]) for x in range(1, len(level))])):
            continue

        safe += 1

    print(safe)


def part_2():
    puzzle_in = open('inputs/2-2.txt', 'r').read()
    levels = list(map(lambda ln: list(map(lambda x: int(x), ln.split())), puzzle_in.split('\n')))

    safe = 0
    for level in levels:
        for removed_idx in range(len(level)):
            lvl = level[:removed_idx] + level[removed_idx + 1:]

            dirs = list(map(lambda v: 1 if v > 0 else 0, [lvl[x] - lvl[x - 1] for x in range(1, len(lvl))]))

            if dirs.count(dirs[0]) != len(dirs):
                continue

            if not all(map(lambda v: True if 1 <= v <= 3 else False,
                           [abs(lvl[x] - lvl[x - 1]) for x in range(1, len(lvl))])):
                continue

            safe += 1
            break

    print(safe)

