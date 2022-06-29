# https://www.acmicpc.net/problem/7576

import sys
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

M, N = map(int, input().split())
B = []
for _ in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))

def bfs():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if B[i][j] == 1:
                queue.append((i, j))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if B[ny][nx] > 0 or B[ny][nx] < 0:
                continue
            B[ny][nx] = B[y][x] + 1
            queue.append((ny, nx))

    ans = 0
    for i in range(N):
        for j in range(M):
            if B[i][j] == 0:
                return -1
            if B[i][j] > ans:
                ans = B[i][j]

    return ans - 1

print(bfs())
