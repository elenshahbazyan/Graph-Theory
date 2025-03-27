from collections import defaultdict, deque


def topological_sort(graph, V):
    in_degree = {i: 0 for i in range(V)}
    for u in graph:
        for v, _ in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in in_degree if in_degree[u] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)

        for v, _ in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return topo_order


def longest_path_dag(graph, V, source):
    topo_order = topological_sort(graph, V)
    dist = {i: float('-inf') for i in range(V)}
    dist[source] = 0

    for u in topo_order:
        if dist[u] != float('-inf'):
            for v, weight in graph[u]:
                if dist[u] + weight > dist[v]:
                    dist[v] = dist[u] + weight

    return dist


graph = {
    0: [(1, 5), (2, 3)],
    1: [(3, 6), (2, 2)],
    2: [(3, 7)],
    3: []
}

V = 4
source = 0

distances = longest_path_dag(graph, V, source)

print(f"Longest distances from node {source}:")
for node, distance in distances.items():
    print(f"Node {node}: {distance}")
