import math


def part_1():
    puzzle_input = open('inputs/5-1.txt', 'r').read().split('\n')
    sep = puzzle_input.index("")

    rules, updates = puzzle_input[:sep], puzzle_input[sep+1:]
    rules = [(int(rule.split('|')[0]), int(rule.split('|')[1])) for rule in rules]
    updates = [[int(num) for num in update] for update in list(map(lambda update: update.split(','), updates))]

    total = 0

    def in_order(update):
        nonlocal rules
        for before, after in rules:
            if before in update and after in update:
                if update.index(before) > update.index(after):
                    return False

        return True

    for update in updates:
        if in_order(update):
            total += update[len(update)//2]

    print(total)


def part_2():
    puzzle_input = open('inputs/5-2.txt', 'r').read().split('\n')
    sep = puzzle_input.index("")

    rules, updates = puzzle_input[:sep], puzzle_input[sep + 1:]
    rules = [(int(rule.split('|')[0]), int(rule.split('|')[1])) for rule in rules]
    updates = [[int(num) for num in update] for update in list(map(lambda update: update.split(','), updates))]

    total = 0

    def in_order(update):
        nonlocal rules
        for before, after in rules:
            if before in update and after in update:
                if update.index(before) > update.index(after):
                    return False

        return True

    def put_in_order(update):
        nonlocal rules
        while not in_order(update):
            for before, after in rules:
                if before in update and after in update:
                    if update.index(before) > update.index(after):
                        update.pop(update.index(before))
                        update.insert(update.index(after), before)

    for update in updates:
        if not in_order(update):
            put_in_order(update)
            total += update[len(update) // 2]

    print(total)


if __name__ == '__main__':
    part_2()
