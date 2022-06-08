# https://www.acmicpc.net/problem/1475

import sys


def add_set(L):
    for i in range(10):
        L[i] += 1
    return L

def solution(N, L):
    count = 0
    for num in N:
        if (int(num) == 6):
            if (L[6] == 0 and L[9] > 0):
                L[9] -= 1
                continue
        if (int(num) == 9):
            if (L[9] == 0 and L[6] > 0):
                L[6] -= 1
                continue
        if not L[int(num)]:
            add_set(L)
            count += 1
        L[int(num)] -= 1
    print(count)

if __name__=='__main__':
    N = sys.stdin.readline().strip()
    L = [0 for _ in range(10)]
    solution(N, L)
