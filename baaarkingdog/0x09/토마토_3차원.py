# https://www.acmicpc.net/problem/7569

import sys
from collections import deque


dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, sys.stdin.readline().split())
B = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        B[i].append(list(map(int, sys.stdin.readline().split())))

def bfs():
    queue = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if B[i][j][k] == 1:
                    queue.append((i, j, k))

    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if nz < 0 or nz >= H or ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if B[nz][ny][nx] > 0 or B[nz][ny][nx] < 0:
                continue
            B[nz][ny][nx] = B[z][y][x] + 1
            queue.append((nz, ny, nx))

    ans = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if B[i][j][k] == 0:
                    return -1
                if B[i][j][k] > ans:
                    ans = B[i][j][k]

    return ans - 1

print(bfs())

# 처음 다뤄보는 3차원 배열.
# 3차원 배열을 이런 방식으로 저장하는군...
