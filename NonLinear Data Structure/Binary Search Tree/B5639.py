#stack 사용하려다 실패
tree = {}
n = []
while True:
    try:
        n.append(int(input()))
    except:
        break

# for i in range(1, len(n)+1):
#     # print(n[i-1])
#     # print(n[i])
#     # print("---------------------")
#     if n[i-1] > n[i]:
#         stack.append(n[i])
#     else:
#         if len(stack) != 1:
#             print(stack.pop())
#             print(n[i])
#         else:
#             print(stack.pop())
stack = []
stack2 = []

while True:
    i = 1
    if n[i] > n[0]:
        stack2.append(n[i])
    else:
        stack.append(n[i])
    i = i + 1

stack.sort()

while True:
    if len(stack) != 0:
        print(stack.pop())
    else:
        if len(stack2) != 0:
            print(stack2.pop())