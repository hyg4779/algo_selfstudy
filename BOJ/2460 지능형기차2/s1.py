train = [0]*10
a, b = map(int, input().split())
ans = 0
train[0] = b
for idx in range(1, 10):
    a, b = map(int, input().split())
    train[idx] += b - a + train[idx-1]
    ans = max(ans, train[idx])

print(ans)