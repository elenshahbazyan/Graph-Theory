def dfs(at, graph, visited):
    if visited[at]:
        return
    visited[at] = True
    neighbours = graph[at]
    for next_node in neighbours:
        dfs(next_node, graph, visited)

n = 6
g = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

visited = [False] * n
dfs(0, g, visited)
print("Visited nodes:", visited)
