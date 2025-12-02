import sys


def part_1(rotations, pos = 50):
    count = 0

    for (dir, val) in rotations:
        if dir == 'R':
            pos += val
        if dir == 'L':
            pos -= val
        pos %= 100
        if pos == 0:
            count += 1

    return count

def part_2(rotations, pos = 50):
    count = 0

    for (dir, val) in rotations:
        if dir == 'R':
            pos += val
        if dir == 'L':
            pos -= val
        count += abs(pos) // 100
        if pos <= 0 and pos + val != 0:
            count += 1
        pos %= 100

    return count


if __name__ == "__main__":
    rotations = [(line[0], int(line[1:])) for line in sys.stdin]
    print(f"Part 1: {part_1(rotations)}")
    print(f"Part 2: {part_2(rotations)}")
