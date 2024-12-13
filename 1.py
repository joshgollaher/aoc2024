

def part_1():
    puzzle_in = open('inputs/1-1.txt', 'r').read()
    lhs, rhs = zip(*list(map(lambda ln: ln.split(), puzzle_in.split('\n'))))
    lhs = list(sorted(map(lambda x: int(x), lhs)))
    rhs = list(sorted(map(lambda x: int(x), rhs)))

    print(sum([abs(lhs[x] - rhs[x]) for x in range(len(lhs))]))


def part_2():
    puzzle_in = open('inputs/1-2.txt', 'r').read()
    lhs, rhs = zip(*list(map(lambda ln: ln.split(), puzzle_in.split('\n'))))
    lhs = list(sorted(map(lambda x: int(x), lhs)))
    rhs = list(sorted(map(lambda x: int(x), rhs)))

    sim_score = 0

    for x in lhs:
        sim_score += x * sum(map(lambda v: 1 if v > 0 else 0, filter(lambda v: v == x, rhs)))

    print(sim_score)
