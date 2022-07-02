# https://www.acmicpc.net/problem/4179

import sys
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

R, C = map(int, sys.stdin.readline().split())
M = [list(sys.stdin.readline().strip()) for _ in range(R)]
JQ, FQ = deque(), deque()

for i in range(C):
    for j in range(R):
        if M[j][i] == 'F':
            FQ.append((j, i))
            M[j][i] = 0
        if M[j][i] == 'J':
            JQ.append((j, i))
            M[j][i] = 0

def bfs():
    while FQ:
        y, x = FQ.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or nx >= C or ny < 0 or ny >= R:
                continue
            if (isinstance(M[ny][nx], int) and M[ny][nx] >= 0) or M[ny][nx] == '#':
                continue
            M[ny][nx] = M[y][x] + 1
            FQ.append((ny, nx))

    while JQ:
        y, x = JQ.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or nx >= C or ny < 0 or ny >= R:
                return M[y][x] + 1
            if M[ny][nx] == '#':
                continue
            if (isinstance(M[ny][nx], int) and isinstance(M[y][x], int) and M[ny][nx] <= M[y][x] + 1):
                continue
            M[ny][nx] = M[y][x] + 1
            JQ.append((ny, nx))
    return "IMPOSSIBLE"

print(bfs())

# -------------------------------------------------------
# 더 좋은 코드:

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while f_queue:    # fire BFS
        x, y = f_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue

            if f_visited[nx][ny] != 0 or graph[nx][ny] == '#':
                continue

            f_visited[nx][ny] = f_visited[x][y] + 1
            f_queue.append((nx, ny))

    while j_queue:    # jihoon BFS
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                return j_visited[x][y] + 1    # escape map

            if j_visited[nx][ny] != 0 or graph[nx][ny] == '#' or (f_visited[nx][ny] != 0 and f_visited[nx][ny] <= j_visited[x][y]+1):    # important code
                continue

            j_visited[nx][ny] = j_visited[x][y] + 1
            j_queue.append((nx, ny))

    return 'IMPOSSIBLE'    # not escape map

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
f_queue, j_queue = deque(), deque()    # declare fire, jihoon queue
f_visited, j_visited = [[0] * C for _ in range(R)], [[0] * C for _ in range(R)]    # declare fire, jihoon visited

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':
            f_queue.append((i, j))
        elif graph[i][j] == 'J':
            j_queue.append((i, j))
print(bfs())


# ROW, COLUMN 설정을 잘못해서 한동안 인덱스 에러로 뻘짓을 했다...
# 처음 시도에 잘 안돼서 바킹독님 해설을 보며 풀이를 하였음.
# 아직도 해설에 의존하는 풀이 실력... 성장하고 싶다.
