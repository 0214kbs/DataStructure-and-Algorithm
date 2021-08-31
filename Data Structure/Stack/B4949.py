import sys


def balance_world(string):
    dic = {
        ')':'(',
        ']':'['
    }
    stack = []

    for c in string:
        if c in dic.values():
            stack.append(c)
            # print(stack)
        elif c in dic and stack:
            if stack[-1] == dic[c]:
                # print(c)
                stack.pop()
                # print(stack)
            else:
                return False
        if c == '.' :
            if not stack:
                return True
            else:
                return False


# s = sys.stdin.readline
s = input()
if balance_world(s):
    print("yes")
else:
    print("no")
