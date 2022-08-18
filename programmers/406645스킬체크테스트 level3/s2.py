from collections import deque

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(rectangle, r, c, a, b):
    answer = 2500

    arr = [[0 for _ in range(51)] for _ in range(51)]
    visit = [[0 for _ in range(51)] for _ in range(51)]
    sr, sc = 51, 51
    now = 0

    for x1, y1, x2, y2 in rectangle:
        now += 1
        arr[x1][y1], arr[x1][y2], arr[x2][y1], arr[x2][y2] = now, now, now, now
        x, y = x1, y1
        if x < sr:
            sr, sc = x, y

        idx = 0
        while idx < 4:
            x, y = x+direct[idx][0], y+direct[idx][1]
            if arr[x][y] == now:
                idx += 1
            else:
                arr[x][y] = now

    # 아웃라인 그리기
    p = 0
    flag = True
    while flag:

        for next in [p+1, p, p-1]:
            nr, nc = sr+direct[next%4][0], sc+direct[next%4][1]
            if 0 <= nr < 51 and 0 <= nc < 51 and arr[nr][nc]:
                if arr[nr][nc] == 100:
                    flag = False
                sr, sc = nr, nc
                arr[sr][sc] = 100
                p = next
                break

    # 아웃라인 따라 다니기
    visit[r][c] = 1
    Q = deque([(r, c, 0)])
    while Q:
        i, j, cnt = Q.popleft()

        if i==a and j==b:
            answer = min(cnt, answer)
            continue

        for p in range(4):
            d = direct[p]
            ni, nj = i+d[0], j+d[1]
            if 0 <= ni < 51 and 0 <= nj < 51 and not visit[ni][nj] and arr[ni][nj] == 100:
                visit[ni][nj] = 1
                Q.append((ni, nj, cnt+1))


    return answer

print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))