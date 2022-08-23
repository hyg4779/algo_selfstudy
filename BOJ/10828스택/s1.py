import sys
input = sys.stdin.readline

n = int(input())
arr = [-1]*(n+1)
top = -1

for i in range(n):
    comm = input().rstrip()

    if comm[-1].isdigit():
        tmp, num = comm.split()
        top += 1
        arr[top] = num

    else:
        if comm == 'pop':
            if top == -1:
                print(-1)
            else:
                print(arr[top])
                top -= 1
        elif comm == 'size':
            print(top+1)
        elif comm == 'empty':
            print(1 if top == -1 else 0)
        else:       # top
            print(arr[top])
