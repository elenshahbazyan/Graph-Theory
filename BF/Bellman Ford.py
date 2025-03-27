class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


def bellman_ford(vertices, edges, source):
    INF = float('inf')
    distance = {v: INF for v in range(vertices)}
    distance[source] = 0

    for _ in range(vertices - 1):
        for edge in edges:
            if distance[edge.u] + edge.weight < distance[edge.v]:
                distance[edge.v] = distance[edge.u] + edge.weight

    for _ in range(vertices - 1):
        for edge in edges:
            if distance[edge.u] + edge.weight < distance[edge.v]:
                distance[edge.v] = -INF

    return distance

graph_edges = [
    Edge(0, 1, 3),
    Edge(0, 2, 5),
    Edge(1, 2, -2),
    Edge(1, 3, 6),
    Edge(2, 3, 1)
]
vertices = 4
source_vertex = 0

distances = bellman_ford(vertices, graph_edges, source_vertex)
print("Shortest distances from source vertex:")
for v in range(vertices):
    print(f"Vertex {v}: {distances[v]}")