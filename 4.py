

def part_1():
    puzzle_in = open('inputs/4-1.txt', 'r').read()
    grid = puzzle_in.split('\n')
    num = 0

    def line(x: int, y: int, dx: int, dy: int):
        nonlocal grid

        if x + dx * 3 >= len(grid[0]) or x + dx * 3 < 0 or y + dy * 3 >= len(grid) or y + dy * 3 < 0:
            return False

        match (grid[y][x], grid[y + dy][x + dx], grid[y + dy * 2][x + dx * 2], grid[y + dy * 3][x + dx * 3]):
            case ("X", "M", "A", "S"):
                return True
            case _:
                return False

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            num += sum([
                line(col, row, 1, 0),
                line(col, row, 1, 1),
                line(col, row, 0, 1),
                line(col, row, -1, 1),
                line(col, row, -1, 0),
                line(col, row, -1, -1),
                line(col, row, 0, -1),
                line(col, row, 1, -1)
            ])

    print(num)


def part_2():
    puzzle_in = open('inputs/4-1.txt', 'r').read()
    grid = puzzle_in.split('\n')
    num = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if col + 2 >= len(grid[0]):
                continue
            if row + 2 >= len(grid):
                continue

            pattern = (
                grid[row][col],
                grid[row][col + 2],
                grid[row + 1][col + 1],
                grid[row + 2][col],
                grid[row + 2][col + 2]
            )

            match pattern:
                case ('M', 'S', 'A', 'M', 'S'):
                    num += 1
                case ('S', 'M', 'A', 'S', 'M'):
                    num += 1
                case ('M', 'M', 'A', 'S', 'S'):
                    num += 1
                case ('S', 'S', 'A', 'M', 'M'):
                    num += 1
    print(num)
