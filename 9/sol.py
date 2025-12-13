import sys


def rec(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def part_1(points):
    largest = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            largest = max(largest, rec(points[i], points[j]))
    return largest

def check_crossings(points, a, b, vertical, strict=False):
    x, y = vertical, (vertical + 1) % 2
    crossings = []
    for k in range(-1, len(points) - 1):
        if (
            points[k][x] == points[k + 1][x] 
            and min(a[x], b[x]) < points[k][x] < max(a[x], b[x])
            and (
                (strict and min(points[k][y], points[k + 1][y]) < a[y] < max(points[k][y], points[k + 1][y]))
                or (not strict and min(points[k][y], points[k + 1][y]) <= a[y] <= max(points[k][y], points[k + 1][y]))
            )
        ):
            if not strict and a[y] == min(points[k][y], points[k + 1][y]):
                if min(points[k][y], points[k + 1][y]) + 1 > max(a[y], b[y]):
                    continue
            if not strict and a[y] == max(points[k][y], points[k + 1][y]):
                if max(points[k][y], points[k + 1][y]) - 1 < min(a[y], b[y]):
                    continue
            crossings.append(points[k][x])
    return crossings

def check_vertical(points, a, b):
    # Check for horizontal lines crossing the vertical lines of the rectangle
    if len(check_crossings(points, a, b, 1)): return True
    if len(check_crossings(points, b, a, 1)): return True
    return False

def check_horizontal(points, a, b):
    # Check for vertical lines crossing the horizontal lines of the rectangle
    if len(check_crossings(points, a, b, 0)): return True
    if len(check_crossings(points, b, a, 0)): return True
    return False

def check_inside(points, i, j):
    # print(points[i], points[j], rec(points[i], points[j]))
    p = [(points[i][0] + points[j][0]) // 2, (points[i][1] + points[j][1]) // 2]
    q = [0, p[1]]
    return len(check_crossings(points, q, p, 0, strict=True)) % 2 == 1

def is_valid(points, i, j):
    if check_horizontal(points, points[i], points[j]): return False
    if check_vertical(points, points[i], points[j]): return False
    return check_inside(points, i, j)

def part_2(points):
    largest = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if rec(points[i], points[j]) > largest:
                if is_valid(points, i, j):
                    largest = rec(points[i], points[j])
    return largest


if __name__ == "__main__":
    points = [list(map(int, line.split(','))) for line in sys.stdin]

    print(f"Part 1: {part_1(points)}")
    print(f"Part 2: {part_2(points)}")
