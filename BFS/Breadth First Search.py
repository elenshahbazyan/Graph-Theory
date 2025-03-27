from collections import deque

def bfs(s, e, n, g):
    prev = solve(s, n, g)
    return reconstructPath(s, e, prev)


def solve(s, n, g):
    q = deque([s])
    visited = [False] * n
    visited[s] = True
    prev = [None] * n

    while q:
        node = q.popleft()
        neighbours = g[node]

        for next_node in neighbours:
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True
                prev[next_node] = node

    return prev


def reconstructPath(s, e, prev):
    path = []
    at = e

    while at is not None:
        path.append(at)
        at = prev[at]

    path.reverse()

    if path[0] == s:
        return path
    return []

n = 6
g = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

s = 0
e = 5

path = bfs(s, e, n, g)
print("Path from {} to {}: {}".format(s, e, path))
