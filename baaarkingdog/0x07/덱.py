# https://www.acmicpc.net/problem/10866

import sys


class Deque:
    def __init__(self):
        MX = 1000000
        self.deque = [0] * (2 * MX + 1)
        self.head = MX
        self.tail = MX

    def push_front(self, n):
        self.deque[self.head] = n
        self.head -= 1

    def push_back(self, n):
        self.tail += 1
        self.deque[self.tail] = n

    def pop_front(self):
        if self.head == self.tail:
            return -1

        self.head += 1
        return self.deque[self.head]

    def pop_back(self):
        if self.head == self.tail:
            return -1

        self.tail -= 1
        return self.deque[self.tail + 1]
    
    def d_size(self):
        return self.tail - self.head

    def d_empty(self):
        if self.head == self.tail:
            return 1
        return 0

    def d_front(self):
        if self.head == self.tail:
            return -1
        return self.deque[self.head + 1]

    def d_back(self):
        if self.head == self.tail:
            return -1
        return self.deque[self.tail]

if __name__=='__main__':
    N = int(input())
    deque = Deque()
    for _ in range(N):
        OP = list(sys.stdin.readline().split())
        if OP[0] == "push_front":
            deque.push_front(OP[1])
        if OP[0] == "push_back":
            deque.push_back(OP[1])
        if OP[0] == "pop_front":
            print(deque.pop_front())
        if OP[0] == "pop_back":
            print(deque.pop_back())
        if OP[0] == "size":
            print(deque.d_size())
        if OP[0] == "empty":
            print(deque.d_empty())
        if OP[0] == "front":
            print(deque.d_front())
        if OP[0] == "back":
            print(deque.d_back())


# head와 tail의 움직임에서 시작 지점 가운데가 비어버리는 경우를 조심하기.
