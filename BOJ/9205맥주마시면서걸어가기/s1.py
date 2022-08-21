from collections import deque
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    home = list(map(int, input().split()))
    graph = [list(map(int, input().split())) for _ in range(n)]
    fest = list(map(int, input().split()))

    visit = [0]*(n+1)

    Q = deque([(home[0], home[1])])
    while Q:
        x, y = Q.popleft()

        if abs(x-fest[0]) + abs(y-fest[1]) <=1000:
            print('happy')
            break

        for i in range(n):
            if not visit[i]:
                r, c = graph[i]
                if abs(x-r)+abs(y-c)<=1000:
                    Q.append((r, c))
                    visit[i] = 1
    else:
        print('sad')