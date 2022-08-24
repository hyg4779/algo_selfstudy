import sys
input = sys.stdin.readline

n = int(input())
ksg = [int(input()) for _ in range(n)]
ksg.sort(reverse=True)
ans = 0
for i in range(0, n-2, 3):
    ans += ksg[i] + ksg[i+1]

if n%3 == 1:
    ans += ksg[-1]
elif n%3:
    ans += ksg[-1] + ksg[-2]
print(ans)