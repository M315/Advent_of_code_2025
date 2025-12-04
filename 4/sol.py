import sys


def accessible(m, i, j):
    if m[i][j] != '@':
        return 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if m[ni][nj] == '@':
            count += 1
    return count < 4

def extend_map(m):
    for i in range(len(m)):
        m[i] = list('.' + m[i] + '.')
    m.insert(0, ['.'] * len(m[0]))
    m.append(['.'] * len(m[0]))

    return m

def part_1(m):
    count = 0
    for i in range(1, len(m) - 1):
        for j in range(1, len(m[0]) - 1):
            count += accessible(m, i, j)

    return count

def part_2(m):
    total = 0

    removed = 1
    while removed > 0:
        removed = 0
        for i in range(1, len(m) - 1):
            for j in range(1, len(m[0]) - 1):
                if accessible(m, i, j):
                    removed += 1
                    m[i][j] = '.'
        total += removed

    return total


if __name__ == "__main__":
    m = [ line.strip() for line in sys.stdin ]
    m = extend_map(m)
    print(f"Part 1: {part_1(m)}")
    print(f"Part 2: {part_2(m)}")
