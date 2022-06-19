# https://www.acmicpc.net/problem/1021

import sys
from collections import deque


def main():
    N, M = map(int, input().split())
    L = list(map(int, sys.stdin.readline().split()))
    dq = deque([i for i in range(1, N+1)])
    
    count = 0
    for n in L:
        while True:
            if dq[0] == n:
                dq.popleft()
                break
            if dq.index(n) <= len(dq) // 2:
                dq.rotate(-1)
            else:
                dq.rotate(1)
            count += 1
    print(count)

if __name__ == "__main__":
    main()


# 최솟값을 찾기 위해선 타겟이 앞과 뒤 중 어느 쪽이 더 가까운지 판단해야 한다.
