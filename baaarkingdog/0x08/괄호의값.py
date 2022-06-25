# https://www.acmicpc.net/problem/2504

import sys


def solve():
    string = sys.stdin.readline().strip()
    stack = []
    value = 0
    tmp = 1

    for i, ch in enumerate(string):
        if string[i] == '(':
            tmp *= 2
            stack.append(ch)
        elif string[i] == '[':
            tmp *= 3
            stack.append(ch)
        elif string[i] == ')':
            if not len(stack) or stack[-1] == '[':
                return 0
            if string[i-1] == '(':
                value += tmp
            stack.pop()
            tmp /= 2
        else:
            if not len(stack) or stack[-1] == '(':
                return 0
            if string[i-1] == '[':
                value += tmp
            stack.pop()
            tmp /= 3

    if len(stack):
        return 0
    else:
        return int(value)

print(solve())


# 누적곱?을 이용한 바킹독의 풀이
# 우선 스택을 쌓으며 값을 곱해간다. 그리고 조건이 만족되면 총합에 더한다.
# 조건: 바로 이전 문자열이 서로 짝이 맞는 경우.
# 조건에 만족되지 않으면 누적된 곱을 다시 원래대로 돌려놓는다.
# 즉, 괄호가 가장 깊어지는 지점까지 계속 값을 누적한 후,
# 가장 깊은 상태에서 괄호가 닫히는 순간, 그 값을 총합에 더한다.
# 나머지는 괄호를 계속 닫으며(pop하며) 값을 돌려놓는 과정.
# 이번 문제도 한 번에 풀지 못했지만, 굉장히 재미있는 알고리즘인 것 같다.
