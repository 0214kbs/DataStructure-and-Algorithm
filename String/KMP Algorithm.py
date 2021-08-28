str = "abbabbaba"
pat = "aba"
failure=[0]*(len(pat)+1)
# 패턴 실패 함수
def fail(pat):
    # failure = []
    n = len(pat)
    failure[0] = -1
    for j in range(1, n):
        i = failure[j-1]
        while pat[j] != pat[i + 1] and i >= 0:
            i = failure[i]
        if pat[j] == pat[i + 1]:
            failure[j] = i + 1
        else:
            failure[j] = -1

def pMatch(str, pat):
    i, j = 0, 0
    len_s = len(str)
    len_p = len(pat)
    while i < len_s and j < len_p:
        if str[i] == pat[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = failure[j-1] + 1
    return (i - len_p) if j == len_p else -1

pMatch(str, pat)

print(failure)
print(pMatch(str,pat))