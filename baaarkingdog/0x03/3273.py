# https://www.acmicpc.net/problem/3273

import sys


def solution(n, L, x):
    C = [0 for _ in range(2000000)]
    count = 0;
    for i in L:
        if (C[x - i] == 1):
            count += 1
        C[i] = 1
    return (count)

if __name__=='__main__':
    n = int(input())
    L = list(map(int, sys.stdin.readline().split()))
    x = int(input())
    print(solution(n, L, x))
