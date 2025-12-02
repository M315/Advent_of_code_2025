import sys

def count_silly(a, b, start = 1):
    silly = []
    while int(str(start) + str(start)) <= b:
        candidate = int(str(start) + str(start))
        if candidate >= a:
            silly.append(candidate)
        start += 1
    return silly

def count_super_silly(a, b, start = 1):
    silly = set()
    while int(str(start) + str(start)) <= b:
        for times in range(2, len(str(b)) + 1):
            candidate = int(str(start) * times)
            if a <= candidate <= b:
                silly.add(candidate)
            if candidate > b: break
        start += 1
    return silly

def part_1(ids):
    invalids = 0
    for (a, b) in ids:
        invalids += sum(count_silly(a, b))
    return invalids

def part_2(ids):
    invalids = set()
    for (a, b) in ids:
        invalids.update(count_super_silly(a, b))
    return sum(invalids)


if __name__ == "__main__":
    ids = [
        [int(id) for id in ids.split("-", 1)]
        for ids in sys.stdin.read().split(',')
    ]
    print(f"Part 1: {part_1(ids)}")
    print(f"Part 2: {part_2(ids)}")
