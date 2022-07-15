import sys

A, B, C = map(int, sys.stdin.readline().split())

mod = []                # 나머지들 리스트
num, cnt = A, 1

while cnt < B:

    tmp = num%C
    if tmp in mod:
        res = tmp
        i, j = mod.index(res), cnt-2

        if i-j == 0:
            print(tmp)
        else:
            print(mod[B%cnt-1])
        break


    mod.append(tmp)
    num *= A
    cnt += 1
