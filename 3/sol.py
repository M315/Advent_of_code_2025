import sys

def best(batteries, n):
    best = list(range(n))
    for (i, a) in enumerate(batteries):
        for pos in range(n):
            if len(batteries[i:i + n - pos]) < n - pos: continue
            if a > batteries[best[pos]] and best[pos] < i:
                best[pos:] = list(range(i, i + n - pos))
                break
    ans = 0
    for bat in best: ans = ans * 10 + batteries[bat]
    return ans

def part_1(batteries):
    return sum(best(bat, 2) for bat in batteries)

def part_2(batteries):
    return sum(best(bat, 12) for bat in batteries)


if __name__ == "__main__":
    batteries = [
        [int(bat) for bat in line.strip()]
        for line in sys.stdin
    ]
    print(f"Part 1: {part_1(batteries)}")
    print(f"Part 2: {part_2(batteries)}")
