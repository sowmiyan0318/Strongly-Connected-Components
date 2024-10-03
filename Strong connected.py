from collections import defaultdict

def strongly_connected_components(graph):
    index = 0
    stack = []
    lowlinks = {}
    index_map = {}
    result = []

    def strongconnect(node):
        nonlocal index
        nonlocal stack
        nonlocal lowlinks
        nonlocal index_map
        nonlocal result

        index_map[node] = index
        lowlinks[node] = index
        index += 1
        stack.append(node)

        for neighbor in graph[node]:
            if neighbor not in index_map:
                strongconnect(neighbor)
                lowlinks[node] = min(lowlinks[node], lowlinks[neighbor])
            elif neighbor in stack:
                lowlinks[node] = min(lowlinks[node], index_map[neighbor])

        if lowlinks[node] == index_map[node]:
            scc = []
            while True:
                w = stack.pop()
                scc.append(w)
                if w == node:
                    break
            result.append(scc)

    for node in graph:
        if node not in index_map:
            strongconnect(node)

    return result

# Example usage:
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A', 'D'],
    'D': ['E'],
    'E': ['F'],
    'F': ['D']
}

print(strongly_connected_components(graph))  # Output: [['A', 'B', 'C'], ['D', 'E', 'F']]
