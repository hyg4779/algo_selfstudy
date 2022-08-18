a, b = map(int, input().split())
ans = 0
train = b
for idx in range(1, 10):
    a, b = map(int, input().split())
    train = train + b - a
    ans = max(ans, train)

print(ans)