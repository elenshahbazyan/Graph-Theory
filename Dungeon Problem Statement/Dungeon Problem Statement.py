from collections import deque


def solve():
    R, C = map(int, input().split())
    matrix = []
    for _ in range(R):
        matrix.append(list(input().strip()))

    start_row, start_col = -1, -1
    for r in range(R):
        for c in range(C):
            if matrix[r][c] == 'S':
                start_row, start_col = r, c
                break
        if start_row != -1:
            break

    dr = [-1, +1, 0, 0]
    dc = [0, 0, +1, -1]

    visited = [[False] * C for _ in range(R)]

    row_queue = deque([start_row])
    col_queue = deque([start_col])

    visited[start_row][start_col] = True

    steps = 0
    found_end = False

    def explore_neighbors(r, c):
        nonlocal found_end
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc] and matrix[nr][nc] != '#':
                    visited[nr][nc] = True
                    if matrix[nr][nc] == 'E':
                        found_end = True
                        return
                    row_queue.append(nr)
                    col_queue.append(nc)

    while row_queue:
        r = row_queue.popleft()
        c = col_queue.popleft()
        matrix[r][c] = 'X'
        print(f"Step {steps}:")
        for row in matrix:
            print("".join(row))
        print()

        if found_end:
            break

        explore_neighbors(r, c)

        steps += 1

    if found_end:
        print(f"Found 'E' after {steps} steps.")
    else:
        print("Could not reach 'E'.")


solve()
