import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
sections = [tuple(map(int, input().split())) for _ in range(k)]

for a, b in sections:
    q, mod = str(round(sum(arr[a-1:b])/(b-a+1), 2)).split('.')
    if len(mod) == 1:
        mod += '0'
    print(f'{q}.{mod}')