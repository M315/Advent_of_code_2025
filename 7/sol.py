import sys


def part_1(m):
    beams = [i for i, c in enumerate(m[0]) if c == 'S']

    splits = 0
    for row in m[1:]:
        new_beams = set()
        for b in beams:
            if row[b] == '^':
                new_beams.add(b - 1)
                new_beams.add(b + 1)
                splits += 1
            else:
                new_beams.add(b)
        beams = new_beams

    return splits

def part_2(m):
    beams = {}
    for i, c in enumerate(m[0]):
        if c == 'S':
            beams[i] = 1

    for row in m[1:]:
        new_beams = {}
        for (b, n) in beams.items():
            if row[b] == '^':
                new_beams[b - 1] = new_beams.get(b - 1, 0) + n 
                new_beams[b + 1] = new_beams.get(b + 1, 0) + n 
            else:
                new_beams[b] = new_beams.get(b, 0) + n 
        beams = new_beams

    return sum(beams.values())


if __name__ == "__main__":
    m = [list(line) for line in sys.stdin]

    print(f"Part 1: {part_1(m)}")
    print(f"Part 2: {part_2(m)}")
