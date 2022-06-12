# https://www.acmicpc.net/problem/10845

import sys


class Queue:
    def __init__(self):
        self.queue = [0] * 1000005
        self.size = 0
        self.head = 0
        self.tail = 0

    def q_push(self, n):
        self.queue[self.tail] = n
        self.size += 1
        self.tail += 1

    def q_pop(self):
        if self.size == 0:
            return -1
        
        self.head += 1
        self.size -= 1
        return self.queue[self.head - 1]
    
    def q_size(self):
        return self.size

    def q_empty(self):
        if self.size == 0:
            return 1
        return 0
    
    def q_front(self):
        if self.size == 0:
            return -1
        return self.queue[self.head]

    def q_back(self):
        if self.size == 0:
            return -1
        return self.queue[self.tail - 1]

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
