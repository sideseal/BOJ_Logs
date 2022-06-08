# https://www.acmicpc.net/problem/10808

import sys


if __name__=='__main__':
    S = sys.stdin.readline().strip()
    L = [0 for _ in range(255)]

    for letter in S:
        L[ord(letter)] += 1

    for i in range(97, 123):
        print(L[i], end=" ")
