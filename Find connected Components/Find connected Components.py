graph = [
    [0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0]
]

n = len(graph)
component_count = 0
components = [-1] * n
visited = [False] * n


def dfs(node, comp_id):
    visited[node] = True
    components[node] = comp_id
    for neighbor in range(n):
        if graph[node][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor, comp_id)

def find_components():
    global component_count
    component_count = 0
    for node in range(n):
        if not visited[node]:
            component_count += 1
            dfs(node, component_count)
    return component_count, components


total, comp_map = find_components()

print("Amount of components:", total)
for comp_id in range(1, total + 1):
    print(f"{comp_id}: ", end="")
    for idx, cid in enumerate(comp_map):
        if cid == comp_id:
            print(idx, end=" ")
    print()
