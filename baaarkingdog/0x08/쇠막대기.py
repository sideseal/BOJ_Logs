# https://www.acmicpc.net/problem/10799

import sys


def solve():
    string = sys.stdin.readline().strip()
    stack = []
    count = 0
    stick = 0

    for ch in string:
        if ch == '(':
            count += 1
            stack.append(ch)
        else:
            if len(stack) and stack[-1] == '(':
                count -= 1
                stick += count
            else:
                count -= 1
                stick += 1
            stack.append(ch)

    return stick

print(solve())

'''
()(((()())(())()))(())
    - -- - - -        
   -- -- --- -- -
  --- -- --- -- -- - -

레이저가 나오면 쌓여 있는 막대 count를 stick에 더하고,
레이저가 아닐 경우, 해당 막대는 끝난 것이기에 stick + 1을 한다.

간단하게 파악하는 일이 어려웠던 문제.
'''
