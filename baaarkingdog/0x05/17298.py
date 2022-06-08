# https://www.acmicpc.net/problem/17298

import sys


def solution(N, A):
    L = list(map(int, sys.stdin.readline().split()))
    S = []
    for i in range(N):
        while S and L[S[-1]] < L[i]:
            A[S.pop()] = L[i]
        S.append(i)

if __name__=='__main__':
    N = int(input())
    A = N * [-1]
    solution(N, A)
    print(*A)
