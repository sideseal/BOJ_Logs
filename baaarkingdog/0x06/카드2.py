# https://www.acmicpc.net/problem/2164

import sys


class Queue:
    def __init__(self):
        self.queue = [0] * 1000001
        self.size = 0
        self.head = 0
        self.tail = 0

    def q_push(self, n):
        self.queue[self.tail] = n
        self.size += 1
        self.tail += 1

    def q_pop(self):
        self.head += 1
        self.size -= 1
        return self.queue[self.head - 1]
    
    def q_size(self):
        return self.size

    def q_front(self):
        return self.queue[self.head]

def throw_and_set(q):
    q.q_pop()
    var = q.q_pop()
    q.q_push(var)
    return q

if __name__=='__main__':
    N = int(input())
    queue = Queue()

    for i in range(1, N+1):
        queue.q_push(i)

    while (queue.size > 1):
        queue = throw_and_set(queue)

    print(queue.q_front())
