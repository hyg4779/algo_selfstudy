N = int(input())
# 공간 크기
arr = [list(map(int, input().split())) for _ in range(N)]
# 공간


def dfs(nr, nc, tr, tc, cnt):       # 상어가 물고기한테 가는 길
    global tmp
    if cnt > tmp:
        return

    if nr == tr and nc == tc:        # 물고기한테 도착했으면 거리 갱신
        tmp = min(cnt, tmp)
        return

    for idx in range(4):
        gr, gc = nr + dr[idx], nc + dc[idx]
        if 0 <= gr < N and 0 <= gc < N and visit[gr][gc] == False and arr[gr][gc] <= shark:
            visit[gr][gc] = True
            dfs(gr, gc, tr, tc, cnt+1)
            visit[gr][gc] = False


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
fishes = []                 # 물고기 수


sr, sc = 0, 0               # 상어 위치

# 오른쪽 아래에서 부터 탐색
for a in range(N):
    for b in range(N):
        if 0 < arr[a][b] < 9:
            fishes.append((a, b))
        elif arr[a][b] == 9:
            sr, sc = a, b       # 아기상어 위치

arr[sr][sc] = 0
result = 0      # 움직인 시간
shark = 2       # 처음 상어의 크기
shark_cnt = 0
while fishes:       # 물고기 씨가 마를 때까지

    # 자기 자신보다 작은 물고기 찾기
    dist = N**2              # 먹을 물고기까지 거리
    fish_cnt = 0            # 먹은 물고기 수
    fr, fc = 0, 0           # 먹을 물고기 위치
    for r, c in fishes:
        if arr[r][c] == 0:continue            # 먹은 물고기 자리면 패스

        fish = arr[r][c]

        if 0 < fish < shark:                      # 현재 물고기가 상어보다 작다면
            fish_cnt += 1                       # 먹을 수 있는 물고기 수
            visit = [[False]*N for _ in range(N)]
            visit[sr][sc] = True
            tmp = N**2                          # 현재 상어와의 거리
            dfs(sr, sc, r, c, 0)                # 현재 상어 위치에서 물고기 까지 거리

            if tmp < dist:     # 해당 물고기를 먹을 수 있고, 거리가 가깝다면
                dist = tmp
                fr, fc = r, c                   # 물고기 위치 갱신

    if fish_cnt == 0:        # 먹을수 있는 물고기가 없다면 멈춤
        break

    result += dist             # 상어 이동
    sr, sc = fr, fc
    arr[fr][fc] = 0         # 물고기 먹음
    shark_cnt += 1

    if shark_cnt == shark:  # 상어크기만큼 먹었다면
        shark += 1          # 상어 크기 증가
        shark_cnt = 0

print(result)