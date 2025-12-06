import sys
import re


def evaluate(nums, op):
    res = nums[0]
    for x in nums[1:]:
        res = eval(f"{res}{op}{x}")
    return res

def part_1(input):
    input = [re.findall(r'([\d\*\+]+)[ \n]', line) for line in input.splitlines()]
    nums, ops = input[:-1], input[-1]

    acc = 0
    for n, op in zip(zip(*nums), ops):
        acc += evaluate(n, op)

    return acc

def parse(input):
    lines = [line[::-1] for line in input.splitlines()]

    problems = []
    problem = [[], '']
    for values in zip(*lines):
        if all(v == ' ' for v in values):
            problems.append(problem)
            problem = [[], '']
            continue
        if values[-1] != ' ': problem[1] = values[-1]
        problem[0].append(''.join(values[:-1]))

    return problems +[problem]

def part_2(input):
    acc = 0
    for n, op in parse(input):
        acc += evaluate(n, op)
    return acc


if __name__ == "__main__":
    input = sys.stdin.read()
    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
