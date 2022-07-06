from collections import deque
N, K = map(int, input().split())        # N의 K번째 약수

arr = deque([])

for i in range(N//2+1, 0, -1):
    if not N%i:arr.append(i)

arr.appendleft(N)

print(0) if len(arr) < K else print(arr[-K])