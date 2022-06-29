# https://www.acmicpc.net/problem/1926

import sys
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
B = []
for _ in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))
V = [[False for _ in range(M)] for _ in range(N)]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    V[a][b] = True
    size = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if not V[ny][nx] and B[ny][nx] == 1:
                queue.append((ny, nx))
                V[ny][nx] = True
                size += 1

    return size

P = []
for i in range(N):
    for j in range(M):
        if not V[i][j] and B[i][j] == 1:
            P.append(bfs(i, j))

if len(P) == 0:
    print(len(P))
    print(0)
else:
    print(len(P))
    print(max(P))
