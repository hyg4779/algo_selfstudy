from collections import deque
n, k = map(int, input().split())

visit = [0 for _ in range(100001)]

Q = deque([n])
answer = 100001

while Q:
    now = Q.popleft()

    if now==k:
        print(visit[now])
        exit()

    for next in (now-1, now+1, now*2):
        if 0 <= next < 100001 and not visit[next]:
            visit[next] = visit[now]+1
            Q.append(next)

print(answer)