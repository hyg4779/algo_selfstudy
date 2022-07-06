from collections import deque

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):          # 상어 위치를 찾아 shark에 저장 후 지도상에 0으로 표시
        if arr[i][j] == 9:
            arr[i][j] = 0
            shark = (i, j)

shark_size = 2          # 처음 상어 크기 2
cnt = 0                 # 현재 크기에서 상어가 먹은 물고기 수
result = 0              # 총 시간

while True:
    Q = deque()
    Q.append(shark)                             # Q에 처음에 상어 위치를 넣어줌
    visited = [[0] * N for _ in range(N)]       # 상어가 움직이는 경로를 +1씩 증가하며 저장할 배열
    visited[shark[0]][shark[1]] = 1             # 처음 상어 위치를 1로 설정
    find = []                                   # 거리가 제일 가까운 물고기들의 위치를 담을 배열
    flag = N ** 2                               # 거리가 제일 가까울 때의 거리를 저장할 변수

    while Q:                                    # Q가 빌 때까지 반복
        r, c = Q.popleft()
        if visited[r][c] > flag:                # 만약 현재 위치가 제일 가까운 물고기보다 커지면 반복 종료
            break

        for d in range(4):                      # 4방향 탐색
            nr = r + dr[d]                      # 상어 크기 이하이면서 방문하지 않은곳을 찾음
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] <= shark_size and not visited[nr][nc]:
                if arr[nr][nc] != 0 and arr[nr][nc] < shark_size:       # 이동할 위치에 물고기가 있고 먹을 수 있으면
                    find.append((nr, nc))                               # find 배열에 위치를 담아주고
                    flag = visited[r][c]                                # flag에 거리 표시
                visited[nr][nc] = visited[r][c] + 1                     # 현재 위치보다 1 크게 방문표시
                Q.append((nr, nc))                                      # Q에 담아줌

    else:                               # Q 탐색에서 먹을 수 있는 물고기를 못찾았으면
        break                           # 반복 종료

    nr = N                              # 물고기를 찾았으면
    nc = N                              # 물고기 인덱스 중 가장 위쪽이면서 왼쪽인 곳을 저장할 변수
    for f in find:                      # 물고기 배열을 순회
        r, c = f
        if r < nr:                      # 위쪽이면 갱신
            nr = r
            nc = c
        elif r == nr and c < nc:        # 위쪽은 같은데 왼쪽이면 갱신
            nr = r
            nc = c

    arr[nr][nc] = 0                     # 이동할 칸의 물고기를 먹어주고
    shark = (nr, nc)                    # 상어 위치를 갱신
    cnt += 1                            # 먹은 물고기를 1증가
    if cnt == shark_size:               # 만약 상어 크기만큼 먹었으면
        cnt = 0                         # 먹은 물고기를 0으로 초기화하고 크기 1 증가
        shark_size += 1
    result += flag                      # 경과한 시간만큼 result에 반영

print(result)
