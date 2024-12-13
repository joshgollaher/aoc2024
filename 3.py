import re


def part_1():
    puzzle_in = open('inputs/3-1.txt', 'r').read()
    print(sum(map(lambda tup: int(tup[0]) * int(tup[1]), re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', puzzle_in))))


def part_2():
    puzzle_in = open('inputs/3-2.txt', 'r').read()
    matches = re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)', puzzle_in)
    total = 0
    in_do = True
    for occurrence in matches:
        if 'do()' in occurrence.group():
            in_do = True
        elif 'don\'t' in occurrence.group():
            in_do = False
        elif in_do:
            operands = list(map(lambda v: int(v), occurrence.group().split('(')[1].split(')')[0].split(',')))
            total += operands[0] * operands[1]

    print(total)


