N = int(input())


for tc in range(N):
    M = int(input())
    res = bin(M)[2:][::-1]

    result = list()
    for i in range(len(res)):
        if res[i] == '1':
            result.append(i)

    print(*result)