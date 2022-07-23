N = int(input())

T, P, dp = [0]*N, [0]*N, [0]*25
for i in range(N):
    T[i], P[i] = map(int, input().split())

for j in range(N):
    if dp[j] > dp[j+1]:
        dp[j+1] = dp[j]
    if dp[j+T[j]] < dp[j]+P[j]:
        dp[j+T[j]] = dp[j]+P[j]

print(dp[N])