N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def vert(mat):      # y축 대칭
    return [line[::-1] for line in mat]


def hori(mat):      # x축 대칭
    return mat[::-1]


def rot(mat, i):
    if i == 1:      # 90
        return [list(line)[::-1] for line in zip(*mat)]

    elif i == 2:    # 270 (-90)
        return [list(line) for line in zip(*mat)][::-1]


def inspect(r, c, mat): # 현재위치 r, c 도형 mat
    global result
    # if mat in memo:     # 이미 한 도형이면 return
    #     return

    # memo.append(mat)
    h = len(mat)        # 세로 길이
    v = len(mat[0])     # 가로 길이

    if N < r + h or M < c + v:    # 격자 밖이면 return
        return

    val = 0
    for i in range(h):
        for j in range(v):
            if 0 <= r+i < N and 0 <= c+j < M:
                val += arr[r+i][c+j]*mat[i][j]

    result = max(val, result)       # 최대값 갱신

tetro = [
    [[1, 1, 1, 1]],             # 1x4
    [[1, 1], [1, 1]],           # 2x2
    [[1, 0], [1, 0], [1, 1]],   # 3x2
    [[1, 0], [1, 1], [0, 1]],   # 3x2
    [[1, 1, 1], [0, 1, 0]]      # 2x3
]

result = 0

for r in range(N):
    for c in range(M):
        for tet in tetro:
            # memo = [tet]
            inspect(r, c, tet)      # 현재 도형

            new = vert(tet)         # y축 대칭
            inspect(r, c, new)

            new = hori(tet)         # x축 대칭, 180도 회전
            inspect(r, c, new)

            new = hori(vert(tet))   # 원점 대칭
            inspect(r, c, new)

            new = rot(tet, 1)       # 시계
            inspect(r, c, new)

            new = rot(tet, 2)       # 반시계
            inspect(r, c, new)

print(result)