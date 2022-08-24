import sys
input = sys.stdin.readline

n = int(input())
tips = [int(input()) for _ in range(n)]
tips.sort(reverse=True)
answer = 0
for i in range(n):
    answer += tips[i] - i if tips[i] - i >= 0 else 0

print(answer)