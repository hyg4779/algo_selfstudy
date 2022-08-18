def wall(n, si):        # 벽 수, 행번호
    global safe


    if n == 3:
        visit = [[False]*M for _ in range(N)]       # visit으로도 gyuns 검사 가능
        matrix = [arr[i][::] for i in range(N)]

        # for r, c in germ:
        #     if matrix[r][c] == 2 and visit[r][c] == False:
        #         queue = [[r, c], ]
        #         visit[r][c] = True
        gyuns = germ[::]

        while gyuns:
            nr, nc = gyuns.pop(0)
            visit[nr][nc] = True
            matrix[nr][nc] = 2

            for idx in range(4):
                gr, gc = nr + dr[idx], nc + dc[idx]
                if 0 <= gr < N and 0 <= gc < M and visit[gr][gc] == False and matrix[gr][gc] == 0:
                    gyuns.append([gr, gc])
                    visit[gr][gc] = True

        cnt = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    cnt += 1

        if cnt > safe:
            safe = cnt
        return

    for i in range(N):
        for j in range(M):
            if i >= si and arr[i][j] == 0:
                arr[i][j] = 1
                wall(n+1, i)
                arr[i][j] = 0

N, M = map(int, input().split())     # 세로 가로
arr = [list(map(int, input().split())) for _ in range(N)]

germ = []

for a in range(N):
    for b in range(M):
        if arr[a][b] == 2:
            germ.append([a, b])

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
'''

'''

safe = 0        # 안전구역
wall(0, 0)
print(safe)