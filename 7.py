import itertools


def part_1():
    puzzle_input = open('inputs/7-1.txt', 'r').read()
    eqs = [line.split(':') for line in puzzle_input.split('\n')]
    eqs = list(map(lambda eqn: [int(eqn[0]), [int(x) for x in eqn[1].strip().split(' ')]], eqs))

    total = 0

    for eq in eqs:
        goal = eq[0]
        operands = eq[1]

        possible_operators = [list(x) for x in itertools.product('*+', repeat=len(operands)-1)]

        for operators in possible_operators:
            value = operands[0]
            for op, num in zip(operators, operands[1:]):
                if op == '+':
                    value += num
                else:
                    value *= num
            if value == goal:
                total += goal
                break
    print(total)


def part_2():
    puzzle_input = open('inputs/7-2.txt', 'r').read()
    eqs = [line.split(':') for line in puzzle_input.split('\n')]
    eqs = list(map(lambda eqn: [int(eqn[0]), [int(x) for x in eqn[1].strip().split(' ')]], eqs))

    total = 0

    for eq in eqs:
        goal = eq[0]
        operands = eq[1]

        possible_operators = [list(x) for x in itertools.product('*+|', repeat=len(operands) - 1)]

        for operators in possible_operators:
            value = operands[0]
            for op, num in zip(operators, operands[1:]):
                if op == '+':
                    value += num
                elif op == '*':
                    value *= num
                elif op == '|':
                    value = int(str(value) + str(num))
            if value == goal:
                total += goal
                break
    print(total)
