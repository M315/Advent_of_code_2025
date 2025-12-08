import sys


def compute_distances(points):
    distance = {}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2 + (points[i][2] - points[j][2])**2
            distance[(i, j)] = dist
    return sorted(list(distance.items()), key=lambda x: x[1])

def make_set(parent, point):
    parent[point] = [point, 1]

def find_set(parent, point):
    if parent[point][0] == point:
        return point
    return find_set(parent, parent[point][0])

def union_sets(parent, a, b):
    a = find_set(parent, a)
    b = find_set(parent, b)
    if a != b:
        if parent[a][1] < parent[b][1]:
            a, b = b, a
        parent[b][0] = a
        parent[a][1] += parent[b][1]

def get_components_size(parent):
    components = {}
    for i in range(len(parent)):
        root = find_set(parent, i)
        components.update({root: parent[root][1]})
    return components.values()

def part_1(points, n):
    distances = compute_distances(points)
    parent = [[i, 1] for i in range(len(points))]
    for _ in range(n):
        (i, j), _ = distances.pop(0)
        union_sets(parent, i, j)
    ans = 1
    for s in sorted(get_components_size(parent), reverse=True)[:3]:
        ans *= s
    return ans

def part_2(points):
    distances = compute_distances(points)
    parent = [[i, 1] for i in range(len(points))]
    while True:
        (i, j), _ = distances.pop(0)
        union_sets(parent, i, j)
        if len(get_components_size(parent)) == 1:
            return points[i][0] * points[j][0]


if __name__ == "__main__":
    points = [
        [int(x) for x in line.split(",")]
        for line in sys.stdin
    ]

    print(f"Part 1: {part_1(points, 1000)}")
    print(f"Part 2: {part_2(points)}")
