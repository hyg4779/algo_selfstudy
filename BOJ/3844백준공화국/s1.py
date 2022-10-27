import sys
sys.setrecursionlimit(10000)


def che(a, b):
    global answer

    if d[a] == False:
        d[a] = set(b)

    else:
        if d[a] & b:
            return
        else:
            d[a] |= b

            if ((a*b)**0.5).is_integer():
                answer = max(answer, (a*b)%10000007)
            else:
                che(a+1, b)
                che(a, b-1)


while True:
    n = int(input())
    if n == 0:
        break
    d = {}
    answer = 0
    che(1, n)

    print(answer)