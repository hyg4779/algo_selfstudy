def draw(array, now, x, y):
    for j in now:
        nx, ny = x, y
        while True:
            nx += direct[j][0]
            ny += direct[j][1]
            if 0 <= nx < n and 0 <= ny < m:
                if array[nx][ny] == 6:
                    break
                if array[nx][ny] == 0:
                    array[nx][ny] = 7
            else:
                break


def dfs(idx, array):
    global answer

    if idx == len(cctv):
        count = 0
        for i in range(n):
            count += array[i].count(0)
        answer = min(answer, count)
        return

    r, c, num = cctv[idx]
    for now_mode in mode[num]:
        arr = [row[:] for row in array]
        draw(arr, now_mode, r, c)
        dfs(idx+1, arr)


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 답, cctv 설치된 곳, 방향
answer = float('inf')
direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

# 사무실, cctv 인덱스와 번호
room, cctv = [], []
# cctv인덱스 추가
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if 0 < line[j] < 6:
            cctv.append((i, j, line[j]))
    room.append(line)

dfs(0, room)
print(answer)