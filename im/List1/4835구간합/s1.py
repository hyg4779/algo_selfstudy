import sys
sys.stdin = open('sample_input.txt')

for tc in range(int(input())):

    # 정수 개수, 구간의 개수
    N, M = map(int, input().split())

    args = list(map(int, input().split()))

    high = 1*M
    low = 10000*M

    for idx in range(N-M+1):
        val = sum(args[idx:idx+M])

        if val > high:
            high = val
        if val < low:
            low = val

    print(f'#{tc+1} {high-low}')