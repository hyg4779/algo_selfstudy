from collections import deque

n = int(input())
graph = []
maxNum = 0

for a in range(n):
    graph.append(list(map(int, input().split())))
    for b in range(n):
        if graph[a][b] > maxNum:
            maxNum = graph[a][b]

direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result = 0
for value in range(maxNum):
    visit = [[0] * n for i in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > value and visit[j][k] == 0:
                Q = deque([(j, k)])
                visit[j][k] = 1

                while Q:
                    x, y = Q.popleft()

                    for d in direct:
                        nx, ny = x + d[0], y + d[1]
                        if 0 <= nx < n and 0 <= ny < n:
                            if graph[nx][ny] > value and visit[nx][ny] == 0:
                                visit[nx][ny] = 1
                                Q.append((nx, ny))
                cnt += 1

    if result < cnt:
        result = cnt

print(result)