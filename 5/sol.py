import sys


def is_fresh(ing, ranges):
    for r in ranges:
        if r[0] <= ing <= r[1]:
            return 1
    return 0

def part_1(ranges, ingredients):
    count = 0
    for ing in ingredients:
        count += is_fresh(ing, ranges)
    return count


def part_2(ranges):
    union = []
    ranges.sort()
    for r in ranges:
        inserted = False
        for c in union:
            if not (r[1] < c[0] or r[0] > c[1]):
                c[0] = min(c[0], r[0])
                c[1] = max(c[1], r[1])
                inserted = True
                break
        if not inserted:
            union.append(r)
    
    count = 0
    for r in union:
        count += r[1] - r[0] + 1

    return count

def parse():
    (ranges, ingredients) = sys.stdin.read().strip().split('\n\n', 1)
    ingredients = [int(x.strip()) for x in ingredients.split('\n')]
    ranges = [[int(x) for x in r.strip().split('-')] for r in ranges.split('\n')]

    return (ranges, ingredients)


if __name__ == "__main__":
    ranges, ingredients = parse()

    print(f"Part 1: {part_1(ranges, ingredients)}")
    print(f"Part 2: {part_2(ranges)}")
