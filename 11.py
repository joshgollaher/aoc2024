from collections import defaultdict
from tqdm import tqdm


def part_1():
    puzzle_in = open('inputs/11-1.txt', 'r').read()
    stones = [int(x) for x in puzzle_in.split()]

    for _ in range(25):
        new_stones = []
        for i, stone in enumerate(stones.copy()):
            if stone == 0:
                new_stones.append(1)
                continue

            digits = len(str(stone))
            if digits % 2 == 0:
                lhs, rhs = int(str(stone)[:digits//2]), int(str(stone)[digits//2:])
                new_stones.append(lhs)
                new_stones.append(rhs)
                continue

            new_stones.append(stone * 2024)
        stones = new_stones

    print(len(stones))


def part_2():
    puzzle_in = open('inputs/11-2.txt', 'r').read()
    stones = defaultdict(int)
    for stone in map(int, puzzle_in.split()):
        stones[stone] += 1

    def blink(stone: int) -> list[int]:
        if stone == 0:
            return [1]

        digits = len(str(stone))
        if digits % 2 == 0:
            lhs, rhs = int(str(stone)[:digits // 2]), int(str(stone)[digits // 2:])
            return [lhs, rhs]

        return [stone * 2024]

    for _ in tqdm(range(75)):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            for result in blink(stone):
                new_stones[result] += count
        stones = new_stones

    print(sum(stones.values()))
