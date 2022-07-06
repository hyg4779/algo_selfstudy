


arr = [[0]*4 for _ in range(4)]

f_idx = [False]*17      # 물고기 방향
f_pos = [False]*17      # 물고기 위치
matrix = list()


def dfs(val, arange, shark, f_idx, f_pos):   # result, 격자, 상어 정보, 물고기 방향 배열, 물고기 위치 배열
    global result

    new_shark = shark[:]            # 상어 정보
    mat = [el[:] for el in arange]  # 새 배열
    new_f_idx = f_idx[:]
    new_f_pos = f_pos[:]

    # 1. 물고기 이동
    for num in range(1, 17):        # num: 물고기 번호
        if new_f_pos[num]==False: continue

        idx = new_f_idx[num]            # 물고기 방향
        fr, fc = new_f_pos[num]         # 물고기 위치
        for d in range(8):
            plus = (d + idx)%8          # 물고기 방향부터 반시계 방향으로 회전 탐색
            sr, sc = fr + dr[plus], fc + dc[plus]                   # 나아갈 방향

            if 0 <= sr < 4 and 0 <= sc < 4 and arr[sr][sc] >= 0:    # 이동할 수 있는 조건
                other = mat[sr][sc]
                if other == 0:              # 빈칸이라면
                    mat[sr][sc], mat[fr][fc] = num, 0
                    new_f_pos[num] = (sr, sc)

                else:                       # 믈고기가 있다면
                    new_f_pos[num], new_f_pos[other] = new_f_pos[other], new_f_pos[num]
                    mat[sr][sc], mat[fr][fc] = mat[fr][fc], mat[sr][sc]
                break

    # 2. 상어 이동
    r, c = new_shark[0:2]               # 상어 위치
    head = new_shark[2]                 # 상어 방향
    possible = []                       # 상어가 먹을 수 있는 물고기 번호

    for p in range(1, 4):
        nr, nc = r + dr[head]*p, c + dc[head]*p                # 진행 방향

        if 0 <= nr < 4 and 0 <= nc < 4 and 0 < mat[nr][nc]:    # 격자 안 and 물고기 있다면
            possible.append(mat[nr][nc])                       # 가능한 물고기 번호 저장

    if not possible:
        if val > result:
            result = max(val, result)
            return

    for food in possible:
        tr, tc = new_f_pos[food]                            # 물고기 위치
        mat[r][c], mat[tr][tc] = 0, -1                      # 상어 자리 움직임
        new_shark = (tr, tc, new_f_idx[food])               # 상어 방향 = 물고기 방향
        new_f_idx[food], new_f_pos[food] = False, False     # 물고기 정보 제거

        dfs(val+food, mat, new_shark, new_f_idx, new_f_pos)

        mat[r][c], mat[tr][tc] = -1, food
        new_f_pos[food], new_f_idx[food] = (tr, tc), new_shark[2]
        new_shark = (r, c, head)


for _ in range(4):
    line = list(map(int, input().split()))                         # 첫줄
    matrix.append([line[0:2], line[2:4], line[4:6], line[6:8]])    # 격자 위치에 물고기 번호와 방향 저장


for a in range(4):
    for b in range(4):
        n, i = matrix[a][b]
        f_idx[n] = i-1                # 물고기 방향 저장
        f_pos[n] = (a, b)             # 물고기 위치 저장
        arr[a][b] = n                 # 격자에 물고기 번호 저장

dr = [-1, -1, 0, 1, 1, 1, 0, -1]        # 8방향
dc = [0, -1, -1, -1, 0, 1, 1, 1]

shark = [0, 0, 0]       # 상어 위치, 방향
f = arr[0][0]           # (0, 0) 물고기 번호
arr[0][0] = -1
shark[2] = f_idx[f]        # 상어 방향
result = f              # 먹은 물고기 번호

f_idx[f] = False        # (0, 0) 정보 제거
f_pos[f] = False


dfs(result, arr, shark, f_idx, f_pos)

print(result)