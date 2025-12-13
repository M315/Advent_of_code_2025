import sys


def bfs(start, goal, graph):
    states = [(start, set(), 1)]
    paths = 0
    while states:
        new_states = {}
        for (state, parents, n) in states:
            parents.add(state)
            if state == goal:
                paths += n
                continue
            for node in graph.get(state, []):
                if node not in parents:
                    p, m = new_states.get(node, [set(), 0])
                    new_states[node] = [p | parents, m + n]
        states = [(state, parents, count) for (state, (parents, count)) in new_states.items()]
    return paths

def part_1(graph):
    return bfs('you', 'out', graph)

def part_2(graph):
    return bfs('svr', 'fft', graph) * bfs('fft', 'dac', graph) * bfs('dac', 'out', graph) \
        + bfs('svr', 'dac', graph) * bfs('dac', 'fft', graph) * bfs('fft', 'out', graph)


if __name__ == "__main__":
    input = [list(line.split(": ")) for line in sys.stdin]
    graph = dict([(key, list(val.strip().split(' '))) for key, val in input])

    print(f"Part 1: {part_1(graph)}")
    print(f"Part 2: {part_2(graph)}")
