import sys
import re
import numpy as np
from scipy.optimize import milp, LinearConstraint


def press_button(state, button):
    new_state = state
    for pos in button:
        new_state ^= 1 << pos
    return new_state

def bfs(start, goal, buttons):
    states = [start]
    visited = set(states)

    steps = 0
    while states:
        next_states = []
        for state in states:
            if state == goal:
                return steps
            for button in buttons:
                new_state = press_button(state, button)
                if new_state not in visited:
                    visited.add(new_state)
                    next_states.append(new_state)
        states = next_states
        steps += 1

def part_1(problems):
    s = 0
    for problem in problems:
        goal = int(''.join(reversed([str(int(x)) for x in problem.goal])), 2)
        s += bfs(0, goal, problem.buttons)
    return s

def sol(problem):
    A = np.zeros((len(problem.buttons), len(problem.joltage)))
    for (i, button) in enumerate(problem.buttons):
        for j in button:
            A[i][j] = 1
    A = A.T
    b = np.array(problem.joltage)

    constraints = LinearConstraint(A, lb=b, ub=b)
    res = milp(c=np.ones(A.shape[1]), constraints=constraints, integrality=np.ones(A.shape[1]))
    np.testing.assert_almost_equal(np.array(problem.joltage), A @ res.x, decimal=12)
    return int(np.round(np.sum(res.x)))

def part_2(problems):
    return sum(sol(problem) for problem in problems)

class Problem:
    def __init__(self, goal, buttons, joltage):
        self.goal = [x == '#' for x in goal]
        self.joltage = list(map(int, joltage.split(',')))
        self.buttons = [
            list(map(int, button[1:-1].split(',')))
            for button in buttons.split(' ')
        ]
    
    def __str__(self):
        return f"Goal: {self.goal}, Buttons: {self.buttons}, Joltage: {self.joltage}"
    
    def __repr__(self):
        return self.__str__()

def parse():
    input = [
        re.findall(r'\[([\.#]+)\] (\(.*\)+) \{(.*)\}', line)[0]
        for line in sys.stdin.read().strip().split('\n')
    ]
    return [
        Problem(goal, buttons, joltage)
        for goal, buttons, joltage in input
    ]

if __name__ == "__main__":
    problems = parse()

    print(f"Part 1: {part_1(problems)}")
    print(f"Part 2: {part_2(problems)}")
