from collections import defaultdict, deque

edges = [
    ('0', '2'), ('0', '6'), ('0', '3'),
    ('1', '4'),
    ('2', '6'),
    ('3', '1'), ('3', '4'),
    ('4', '5'), ('4', '8'),
    ('6', '7'), ('6', '11'),
    ('7', '4'), ('7', '12'),
    ('10', '6'),
    ('9', '10'),
    ('11', '12'),
    ('12', '8')
]

graph = defaultdict(list)
nodes = set()

for src, dest in edges:
    graph[src].append(dest)
    nodes.update([src, dest])

for node in nodes:
    if node not in graph:
        graph[node] = []

def find_topological_ordering(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in graph if in_degree[node] == 0])
    topo_order = []

    while queue:
        current = queue.popleft()
        topo_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == len(graph):
        return topo_order
    else:
        return "topological ordering not possible"

print("Topological Ordering:", find_topological_ordering(graph))
