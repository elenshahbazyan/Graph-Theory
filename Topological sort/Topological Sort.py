def dfs(at, V, visitedNodes, graph):
    V[at] = True
    for neighbor in graph[at]:
        if not V[neighbor]:
            dfs(neighbor, V, visitedNodes, graph)
    visitedNodes.append(at)

def topsort(graph):
    N = len(graph)
    V = [False] * N
    ordering = [0] * N
    i = N - 1
    for at in range(N):
        if not V[at]:
            visitedNodes = []
            dfs(at, V, visitedNodes, graph)
            for nodeId in visitedNodes:
                ordering[i] = nodeId
                i -= 1
    return ordering

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [4],
    3: [5],
    4: [5],
    5: []
}

result = topsort(graph)
print("Topological Sort:", result)
