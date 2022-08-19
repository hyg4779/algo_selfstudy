dr = [0, -1, 1, 0, 0]  # 상하좌우
dc = [0, 0, 0, -1, 1]

# 격자 크기, 상어 번호, 이동 횟수
N, M, K = map(int, input().split())

# 격자
arr = [list(map(int, input().split())) for _ in range(N)]
sharks = dict()    # 상어 별 위치를 담는 dict
s_direct = list(map(int, input().split()))        # 상어 별 현재 방향

visit = [[0]*N for _ in range(N)]               # 상어 별 냄새가 남은 곳 담는 변수

for a in range(N):
    for b in range(N):
        if arr[a][b] == 0: continue
        sharks[arr[a][b]] = (a, b)       # 해당위치 상어 번호에 인덱스 번호 추가 1, 2, 3 ... M
        visit[a][b] = arr[a][b]
        arr[a][b] = K


direction = dict()
for n in range(1, M*4+1):
    # 상어별 상 하 좌 우 우선 탐색방향 배열 입력
    # 1번상어 direction[1~4]
    direction[n] = list(map(int, input().split()))

result = 0

while result < 1000:
    num = 1                             # 상어 번호
    result += 1
    while num <= M:

        if sharks[num] == False:
            num += 1
            continue

        idx = s_direct[num-1]                 # 상어의 방향
        rotate = direction[4*(num-1)+idx]   # 상어의 탐색 순서
        r, c = sharks[num]                  # 상어 위치


        # 빈칸 탐색
        for i in rotate:
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
                sharks[num] = (nr, nc)
                s_direct[num-1] = i
                break

        else:   # 빈 칸을 못 찾았으면
            # 현재 상어의 냄새위치 탐색
            for i in rotate:
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == num:
                    sharks[num] = (nr, nc)
                    s_direct[num-1] = i
                    break

        # 다음 상어 번호
        num += 1
    else:   # 상어 이동이 끝나면 상어가 겹치는 칸 찾기

        for high in range(1, M):
            if sharks[high] == False: continue
            for low in range(high+1, M+1):
                if sharks[high] == sharks[low]:
                    sharks[low] = False

        # 냄새 지속시간 줄이기
        for a in range(N):
            for b in range(N):
                if arr[a][b]:
                    arr[a][b] -= 1
                    if arr[a][b] == 0:
                        visit[a][b] = 0

        for s, p in sharks.items():
            if p == False: continue
            r, c = p
            arr[r][c] = K
            visit[r][c] = s

        cnt = 0         # 남은 상어 수

        for s in sharks.values():
            if s:
                cnt += 1
        if cnt == 1:
            break


else:
    result = -1

print(result)