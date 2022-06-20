# https://www.acmicpc.net/problem/4949

import sys


def solve():
    while True:
        string = sys.stdin.readline().strip('\n')
        if string == '.':
            break
        
        stack = []
        valid = True
        for ch in string:
            if ch == '(' or ch == '[':
                stack.append(ch)
            elif ch == ')':
                if not len(stack) or stack[-1] != '(':
                    valid = False
                    break
                stack.pop()
            elif ch == ']':
                if not len(stack) or stack[-1] != '[':
                    valid = False
                    break
                stack.pop()

        if len(stack):
            valid = False

        if not valid:
            print("no")
        else:
            print("yes")

if __name__ == "__main__":
    solve()


# 바킹독 풀이처럼, 맨 마지막 닫는 괄호에서 가장 최근의 괄호 입력을 체크하는
# 방법은 굉장히 흥미롭다! (인덱싱을 위해 스택이 비었는지도 같이 확인을 해줘야한다.)
