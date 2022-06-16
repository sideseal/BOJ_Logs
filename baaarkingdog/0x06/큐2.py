# https://www.acmicpc.net/problem/18258

import sys
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def q_push(self, n):
        self.queue.append(n)

    def q_pop(self):
        if not self.queue:
            return -1
        return self.queue.popleft()
    
    def q_size(self):
        return len(self.queue)

    def q_empty(self):
        if not self.queue:
            return 1
        return 0
    
    def q_front(self):
        if not self.queue:
            return -1
        return self.queue[0]

    def q_back(self):
        if not self.queue:
            return -1
        return self.queue[-1]

if __name__=='__main__':
    N = int(input())
    queue = Queue()
    for _ in range(N):
        OP = list(sys.stdin.readline().split())
        if OP[0] == "push":
            queue.q_push(OP[1])
        if OP[0] == "pop":
            print(queue.q_pop())
        if OP[0] == "size":
            print(queue.q_size())
        if OP[0] == "empty":
            print(queue.q_empty())
        if OP[0] == "front":
            print(queue.q_front())
        if OP[0] == "back":
            print(queue.q_back())

# 큐를 리스트로 구현할 시 메모리 : 143744 KB, 시간 : 2988 ms
# deque 모듈로 구현할 시 메모리 : 141728 KB, 시간 : 2648 ms
# deque 모듈이 조금 더 빠르다.
