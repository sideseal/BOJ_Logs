# https://www.acmicpc.net/problem/2577

import sys


def find_quotient(num):
    n = 10
    while (num / n >= 10):
        n *= 10
    return (n)

def ft_putnbr(num):
    L = [0 for _ in range(10)]
    q = find_quotient(num)
    while (q > 0):
        n = num // q
        L[n] += 1
        num = num % q
        q = q // 10
    for i in L:
        print(i)

if __name__=='__main__':
    A = int(sys.stdin.readline().strip())
    B = int(sys.stdin.readline().strip())
    C = int(sys.stdin.readline().strip())

    num = A * B * C
    ft_putnbr(num)
