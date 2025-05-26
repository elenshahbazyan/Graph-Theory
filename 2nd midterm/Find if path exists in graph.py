import ast
from collections import defaultdict

def validPath(n, edges, source, destination):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        if node == destination:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False

    return dfs(source)

n = int(input("Enter number of nodes : "))
edges_input = input("Enter edges: ")
source = int(input("Enter source node: "))
destination = int(input("Enter destination node: "))

edges = ast.literal_eval(edges_input)

if validPath(n, edges, source, destination):
    print("Path exists ")
else:
    print("No path found ")