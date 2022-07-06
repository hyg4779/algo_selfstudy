# 버블정렬

args = [55, 7, 78, 12, 42]

for j in range(len(args)-1, 0, -1):
    for i in range(0, j):
        if args[i] > args[i+1]:
            args[i], args[i+1] = args[i+1], args[i]



import sys
sys.stdin = open('sample_input.txt')


for tc in range(int(input())):

    # 정수 N개
    N = int(input())
    args = list(map(int, input().split()))

    max_num = args[0]
    min_num = args[N-1]
    for i in range(1, N):
        if args[i] > max_num:
            max_num = args[i]
        elif args[i] < min_num:
            min_num = args[i]

    print(f'#{tc+1} {max_num-min_num}')
