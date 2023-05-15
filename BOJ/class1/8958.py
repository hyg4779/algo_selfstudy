import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    word = input().strip()
    result = 0
    point = 0
    for i in word:
        if i == 'O':
            point += 1
            result += point
        else:
            point = 0

    print(result)