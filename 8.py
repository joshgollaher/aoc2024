import itertools
import math


def part_1():
    puzzle_in = open('inputs/8-1.txt', 'r').read()
    grid = puzzle_in.split('\n')
    antennae: dict[str, list[tuple[int, int]]] = {}

    def creates_antinode(origin: tuple[int, int], a1: tuple[int, int], a2: tuple[int, int]) -> bool:

        if a1 == origin or a2 == origin:
            return False

        mag_1 = math.sqrt((origin[0] - a1[0]) ** 2 + (origin[1] - a1[1]) ** 2)
        mag_2 = math.sqrt((origin[0] - a2[0]) ** 2 + (origin[1] - a2[1]) ** 2)

        dir_1 = (origin[0] - a1[0]) / mag_1, (origin[1] - a1[1]) / mag_1
        dir_2 = (origin[0] - a2[0]) / mag_2, (origin[1] - a2[1]) / mag_2

        if dir_1[0] != dir_2[0] or dir_1[1] != dir_2[1]:
            return False

        return mag_1 / mag_2 == 2 or mag_2 / mag_1 == 2

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if grid[i][j] != '.':
                if grid[i][j] not in antennae:
                    antennae[grid[i][j]] = []
                antennae[grid[i][j]].append((j, i))
    num_nodes = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            found_antinode = False
            for antennae_type in antennae:
                if len(antennae[antennae_type]) < 2:
                    continue

                perms = itertools.permutations(antennae[antennae_type], 2)
                for antenna_1, antenna_2 in perms:
                    if creates_antinode((j, i), antenna_1, antenna_2):
                        num_nodes += 1
                        found_antinode = True
                        break
                if found_antinode:
                    break

    print(num_nodes)


def part_2():
    puzzle_in = open('inputs/8-2.txt', 'r').read()
    grid = puzzle_in.split('\n')
    antennae: dict[str, list[tuple[int, int]]] = {}

    def creates_antinode(origin: tuple[int, int], a1: tuple[int, int], a2: tuple[int, int]) -> bool:
        if a1 == origin or a2 == origin:
            return True

        # colinear
        dx1 = origin[0] - a1[0]
        dy1 = origin[1] - a1[1]
        dx2 = origin[0] - a2[0]
        dy2 = origin[1] - a2[1]

        return dx1 * dy2 == dx2 * dy1

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if grid[i][j] != '.':
                if grid[i][j] not in antennae:
                    antennae[grid[i][j]] = []
                antennae[grid[i][j]].append((j, i))

    num_nodes = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            found_antinode = False
            for antennae_type in antennae:
                perms = itertools.permutations(antennae[antennae_type], 2)
                for antenna_1, antenna_2 in perms:
                    if creates_antinode((j, i), antenna_1, antenna_2):
                        num_nodes += 1
                        found_antinode = True
                        break
                if found_antinode:
                    break

    print(num_nodes)
