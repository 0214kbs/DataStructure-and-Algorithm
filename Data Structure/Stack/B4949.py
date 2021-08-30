import sys


def balance_world(string):
    stack = []
    for c in string:
        if c == '.':
            break
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            stack.pop()
    if len(stack) == 0:
        print("yes")
    else:
        print("no")


# s = sys.stdin.readline
s = input()
balance_world(s)
