import sys
input = sys.stdin.readline

n = int(input())
bridge = list(map(int, input().split()))

res, now = 0, 0
for i in range(1, n):
    if not now and bridge[i-1] < bridge[i]:
        now = 2
    elif now and bridge[i-1] < bridge[i]:
        now += 1
    elif now and bridge[i-1] >= bridge[i]:
        res = max(res, now)
        now = 0
else:
    res = max(res, now)
print(res)