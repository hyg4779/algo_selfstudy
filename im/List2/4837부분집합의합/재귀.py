import sys
sys.stdin = open('sample_input.txt')


def recur(num, n_sum, cnt):
    if cnt == N:
        if n_sum == K:
            return 1
        else:
            return 0

    rec_sum = 0
    for u in range(num+1, 13):
        rec_sum += recur(u, n_sum+u, cnt+1)
    return rec_sum


for tc in range(int(input())):
    N, K = map(int, input().split())
    cnt = recur(0, 0, 0)
    print(f'#{tc+1} {cnt}')