

def part_1():
    puzzle_input = open('inputs/6-1.txt', 'r').read()
    grid = puzzle_input.split('\n')

    def longest_line(x, y, dx, dy) -> tuple[int, int, int, bool]:
        total = 0
        last_pos = (x, y)

        curr_x, curr_y = x, y
        while True:
            curr_x += dx
            curr_y += dy

            if curr_x < 0 or curr_x >= len(grid[0]) or curr_y < 0 or curr_y >= len(grid):
                return total, last_pos[0], last_pos[1], True

            if grid[curr_y][curr_x] == '#':
                return total, last_pos[0], last_pos[1], False

            if grid[curr_y][curr_x] == 'X':
                continue

            total += 1
            last_pos = (curr_x, curr_y)
            grid[curr_y] = grid[curr_y][:curr_x] + 'X' + grid[curr_y][curr_x + 1:]

    x = y = 0
    for i, row in enumerate(grid):
        if '^' in row:
            x = row.index('^')
            y = i

    direction = [0, -1]
    path_steps = 1

    while True:
        steps_taken, new_x, new_y, offscreen = longest_line(x, y, direction[0], direction[1])
        path_steps += steps_taken

        if offscreen:
            break

        direction[0], direction[1] = -direction[1], direction[0]
        x = new_x
        y = new_y

    print(path_steps)


# Probably faster ways to do this
def part_2():
    puzzle_input = open('inputs/6-1.txt', 'r').read()
    grid = puzzle_input.split('\n')

    pos_x = pos_y = 0
    for i, row in enumerate(grid):
        if '^' in row:
            pos_x = row.index('^')
            pos_y = i

    def halts(x: int, y: int) -> bool:
        direction = (0, -1)
        visited = set()

        while True:
            state = (x, y, direction)
            if state in visited:
                return True
            visited.add(state)

            nx, ny = x + direction[0], y + direction[1]

            if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
                return False

            if grid[ny][nx] == '#':
                dx, dy = direction
                direction = (-dy, dx)
                continue

            x, y = nx, ny

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row == pos_y and col == pos_x) or grid[row][col] == '#':
                continue

            original = grid[row][col]
            grid[row] = grid[row][:col] + "#" + grid[row][col+1:]

            if halts(pos_x, pos_y):
                total += 1
            grid[row] = grid[row][:col] + original + grid[row][col+1:]

    print(total)
