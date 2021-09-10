def push(stack, x):
    stack.append(x)


def pop(stack):
    stack.pop()


def top(stack):
    return stack[-1] if stack else -1


dic = {
    ')': '(',
    ']': '['
}

while True:
    string = input()
    if string == '.':
        break
    else:
        stack = []
        print_value = True

        for c in string:
            if c in dic.values():
                # stack.append(c)
                push(stack, c)
                # print(stack)
            elif c in dic.keys():
                if top(stack) == dic[c] and len(stack) != 0:
                    # stack.pop()
                    pop(stack)
                    # print(stack)
                else:
                    if top(stack) == dic.keys():
                        push(stack, c)
                        break

        if len(stack) == 0:
            print("yes")
        else:
            print("no")
