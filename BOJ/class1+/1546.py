import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))

val = max(scores)
new = map(lambda x: round(x/val * 100, 2), scores)
print(round(sum(new)/n, 2))