import sys
import copy

sys.setrecursionlimit(20000)

def rotate(present):
    p = copy.deepcopy(present)
    return [
        [p[2][0], p[1][0], p[0][0]],
        [p[2][1], p[1][1], p[0][1]],
        [p[2][2], p[1][2], p[0][2]],
    ]

def reflect(present):
    reflection = copy.deepcopy(present)
    for i in range(len(present)):
        reflection[i][0] = present[i][-1]
        reflection[i][-1] = present[i][0]
    return reflection

def valid_positions(present):
    positions = []
    for _ in range(4):
        present = rotate(present)
        if present not in positions:
            positions.append(present)
            positions.append(reflect(present))
    return positions

def add_pice(i, j, present):
    for x in range(len(present)):
        for y in range(len(present[0])):
            if i + x >= len(M) or j + y >= len(M[0]):
                return False
            if present[x][y] == '#' and M[i + x][j + y] == '#':
                return False
    for x in range(len(present)):
        for y in range(len(present[0])):
            if present[x][y] == '#':
                M[i + x][j + y] = '#'
    return True

def remove_pice(i, j, present):
    for x in range(len(present)):
        for y in range(len(present[0])):
            if present[x][y] == '#':
                M[i + x][j + y] = '.'

def backtrack(i, j, counts, space):
    if space < 0:
        return False
    if all(map(lambda x: x == 0, counts)):
        return True
    ni, nj = i + ((j + 1) // len(M[0])), (j + 1) % len(M[0])
    if M[i][j] == '#':
        return backtrack(ni, nj, counts, space)
    for (p, c) in enumerate(counts):
        if c > 0:
            for present in PRESENTS[p]:
                if add_pice(i, j, present):
                    counts[p] -= 1
                    if backtrack(ni, nj, counts, space):
                        return True
                    else:
                        counts[p] += 1
                        remove_pice(i, j, present)
    return backtrack(ni, nj, counts, space - 1)

def fit(dim, counts):
    global M
    M = [['.' for _ in range(dim[1])] for _ in range(dim[0])]
    total_area = sum(count * AREAS[i] for i, count in enumerate(counts))
    space = (dim[0] * dim[1]) - total_area
    return backtrack(0, 0, counts, space)

def part_1(regions):
    return sum(fit(dim, counts) for (dim, counts) in regions)

def part_2():
    return

def parse():
    input = [block for block in sys.stdin.read().split('\n\n')]
    presents, regions = input[:-1], input[-1]
    presents = [list(map(list, present.splitlines()[1:])) for present in presents]
    regions = [list(region.strip().split(':')) for region in regions.splitlines()]
    regions = [[list(map(int, shape.split('x'))), list(map(int, p.strip().split(' ')))] for (shape, p) in regions]

    return presents, regions


if __name__ == "__main__":
    presents, regions = parse()

    global AREAS
    global PRESENTS
    AREAS = [sum(row.count('#') for row in present) for present in presents]
    PRESENTS = [valid_positions(present) for present in presents]

    print(f"Part 1: {part_1(regions)}")
    print(f"Part 2: {part_2()}")
