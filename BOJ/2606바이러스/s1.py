from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0
Q = deque([1])
visit[1] = 1
while Q:
    now = Q.popleft()
    answer += 1
    for i in graph[now]:
        if not visit[i]:
            visit[i] = 1
            Q.append(i)

print(answer-1)ㄴ