graph = {
    '0' : ['2', '6', '3'],
    '1' : ['4'],
    '2' : ['6'],
    '3' : ['1', '4'],
    '4' : ['5', '8'],
    '5' : [],
    '6' : ['7', '11'],
    '7' : ['4', '12'],
    '8' : [],
    '9' : ['10'],
    '10' : ['6'],
    '11' : ['12'],
    '12' : ['8'],
    '13' : []

}



from collections import deque

def FindTopologicalOrdering(graph):
    in_degree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    q = deque([node for node in graph if in_degree[node] == 0])
    order = []

    while q:
        at = q.popleft()
        order.append(at)

        for neighbor in graph[at]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    if len(order) == len(graph):
        return order
    else:
        return -1


print("Topological Ordering:", FindTopologicalOrdering(graph))