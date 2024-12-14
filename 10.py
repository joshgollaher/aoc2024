

def part_1():
    puzzle_input = open('inputs/10-1.txt', 'r').read()
    grid = puzzle_input.split('\n')

    reachable_tops: dict[tuple[int, int], list[tuple[int, int]]] = {}

    def do_trailhead(origin: tuple[int, int], row: int, col: int):
        nonlocal reachable_tops, grid

        num = int(grid[row][col])
        if num == 9:
            if origin in reachable_tops:
                if (row, col) in reachable_tops[origin]:
                    return
            else:
                reachable_tops[origin] = []

            reachable_tops[origin].append((row, col))


        uphill = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0]) and int(grid[r][c]) == num + 1

        if uphill(row, col + 1): do_trailhead(origin, row, col + 1)
        if uphill(row, col - 1): do_trailhead(origin, row, col - 1)
        if uphill(row + 1, col): do_trailhead(origin, row + 1, col)
        if uphill(row - 1, col): do_trailhead(origin, row - 1, col)


    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '0':
                do_trailhead((row, col), row, col)

    print(sum([len(reachable_tops[x]) for x in reachable_tops]))



def part_2():
    puzzle_input = open("inputs/10-2.txt", 'r').read()
    grid = puzzle_input.split('\n')

    reachable_tops: dict[tuple[int, int], list[tuple[int, int]]] = {}

    def do_trailhead(origin: tuple[int, int], row: int, col: int):
        nonlocal reachable_tops, grid

        num = int(grid[row][col])
        if num == 9:
            if origin not in reachable_tops:
                reachable_tops[origin] = []
            reachable_tops[origin].append((row, col))

        uphill = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0]) and int(grid[r][c]) == num + 1

        if uphill(row, col + 1): do_trailhead(origin, row, col + 1)
        if uphill(row, col - 1): do_trailhead(origin, row, col - 1)
        if uphill(row + 1, col): do_trailhead(origin, row + 1, col)
        if uphill(row - 1, col): do_trailhead(origin, row - 1, col)

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '0':
                do_trailhead((row, col), row, col)

    print(sum([len(reachable_tops[x]) for x in reachable_tops]))
