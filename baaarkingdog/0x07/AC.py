# https://www.acmicpc.net/problem/5430

from collections import deque


def normalize(string):
    dq = deque()
    tmp_string = string[1:-1].split(',')
    for ch in tmp_string:
        if ch:
            dq.append(ch)
    return dq

def pprint(status, num_list):
    changed_list = list(num_list)
    num_str = '[' + ','.join(changed_list[::status]) + ']'
    return num_str

def solve():
    p = str(input())
    n = int(input())
    num_list = normalize(str(input()))
    status = 1
    for operation in p:
        if operation == 'R':
            status *= -1
        else:
            if len(num_list) == 0:
                return False
            if status > 0:
                num_list.popleft()
            else:
                num_list.pop()

    return pprint(status, num_list)

def main():
    T = int(input())
    for _ in range(T):
        answer = solve()
        if not answer:
            print("error")
        else:
            print(answer)

if __name__ == "__main__":
    main()
