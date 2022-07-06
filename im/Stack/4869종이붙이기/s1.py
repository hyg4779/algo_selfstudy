import sys
sys.stdin = open('sample_input.txt')


def dp(n):
    global memo

    if n in memo:
        return memo[n]

    dp(n-10)
    dp(n-20)
    memo[n] = memo[n-10] + 2*memo[n-20]


memo = {10: 1, 20: 3}
for tc in range(int(input())):
    N = int(input())

    dp(N)
    print(f'#{tc+1} {memo[N]}')