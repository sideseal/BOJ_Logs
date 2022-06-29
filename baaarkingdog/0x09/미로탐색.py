# https://www.acmicpc.net/problem/2178

import sys
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
B = []
for _ in range(N):
    B.append(list(map(int, sys.stdin.readline().strip())))
D = [[0 for _ in range(M)] for _ in range(N)]

def bfs():
    queue = deque()
    queue.append((0, 0))
    D[0][0] = 1

    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if D[ny][nx] > 0 or B[ny][nx] == 0:
                continue
            D[ny][nx] = D[y][x] + 1
            queue.append((ny, nx))

    return D[N-1][M-1]

print(bfs())
