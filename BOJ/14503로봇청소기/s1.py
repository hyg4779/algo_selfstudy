import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
r, c, idx = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

clean = 0       # 청소한 칸 개수

dr = [-1, 0, 1, 0]  # 북 동 남 서
dc = [0, 1, 0, -1]
# 벽 1 빈칸 0

while True:

    if arr[r][c] != 2:
        arr[r][c] = 2       # 현재위치 청소
        clean += 1          # 청소 + 1

    cnt = 0     # 현재위치에서 탐색 횟수
    while cnt < 4:
        cnt += 1
        idx = (idx-1)%4
        sr, sc = r + dr[idx], c + dc[idx]

        if 1 <= sr < N-1 and 1 <= sc < M-1 and arr[sr][sc] == 0:
            r, c = sr, sc
            break

    else:
        lr, lc = r - dr[idx], c - dc[idx]
        if arr[lr][lc] == 1:
            break
        r, c = lr, lc


print(clean)