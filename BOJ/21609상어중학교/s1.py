from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
INF = float('-inf')
result = 0


def grav():
    flag = True
    while flag:
        flag = False
        for i in range(N-1):
            for j in range(N):
                if arr[i][j] > -1 and arr[i+1][j] == INF:
                    flag = True
                    arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]


while True:
    boom = list()
    visit = [[0]*N for _ in range(N)]
    b_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != INF and not visit[i][j] and arr[i][j] > 0:
                visit[i][j] = 1
                r_vis = [[0]*N for _ in range(N)]
                color, block, rb = arr[i][j], 0, 0
                stack = []
                Q = deque([(i, j)])
                while Q:
                    ni, nj = Q.popleft()
                    stack.append([ni, nj])
                    block += 1
                    for d in direct:
                        si, sj = ni+d[0], nj+d[1]
                        if 0 <= si < N and 0 <= sj < N:
                            if arr[si][sj] == 0 and not r_vis[si][sj]:
                                r_vis[si][sj] = 1
                                rb += 1
                                Q.append((si, sj))
                            elif arr[si][sj] == color and not visit[si][sj]:
                                visit[si][sj] = 1
                                Q.append((si, sj))
                if block > 1:
                    b_cnt = max(b_cnt, block)
                    boom.append([block, rb, stack])

    if boom:
        res = [b for b in boom if b[0]==b_cnt]
        if len(res) > 1:
            ans, rain = [], 0
            for r in res:
                if r[1] >= rain:
                    rain = r[1]
                    ans.append(r)
            res = ans[-1]
        else:
            res = res[-1]
        result += res[0]**2
        stack = res[2]
        for a, b in stack:
            arr[a][b] = INF
        grav()
        arr = list(map(list, zip(*arr)))[::-1]
        grav()

    else:
        break

print(result)