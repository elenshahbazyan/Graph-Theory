import numpy as np


def setup(m):
    n = len(m)
    dp = [[m[i][j] for j in range(n)] for i in range(n)]  # Deep copy of input matrix
    next_matrix = [[None if m[i][j] == float('inf') else j for j in range(n)] for i in range(n)]
    return dp, next_matrix


def floyd_warshall(m):
    n = len(m)
    dp, next_matrix = setup(m)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    next_matrix[i][j] = next_matrix[i][k]

    propagate_negative_cycles(dp, next_matrix, n)

    return dp, next_matrix


def propagate_negative_cycles(dp, next_matrix, n):
    for k in range(n):
        if dp[k][k] < 0:
            for i in range(n):
                for j in range(n):
                    if dp[i][k] != float('inf') and dp[k][j] != float('inf'):
                        dp[i][j] = -float('inf')  # Mark as part of a negative cycle
                        next_matrix[i][j] = None


inf = float('inf')
graph = [
    [0, 3, inf, inf],
    [2, 0, inf, inf],
    [inf, 7, 0, 1],
    [6, inf, inf, 0]
]

shortest_paths, path_matrix = floyd_warshall(graph)
print("Shortest distance matrix:")
for row in shortest_paths:
    print(row)
print("Next matrix for path reconstruction:")
for row in path_matrix:
    print(row)