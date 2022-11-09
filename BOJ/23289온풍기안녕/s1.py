# 격자 크기 n, 구름 m번 이동
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 처음 구름 위치
cloud = {(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)}

# 8방향 이동 서쪽부터 시계방향
dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]


def new_cloud(i, j):
    return True if arr[i][j] >= 2 and not (i, j) in cloud else False


for _ in range(m):
    # 방향과 이동거리
    d, s = map(int, input().split())
    d -= 1
    s %= n

    # 새 구름 목록
    new = set()
    bugs = set()
    for r, c in cloud:
        # 구름들 거리만큼 이동 인덱스
        nr, nc = (r + dx[d]*s)%n, (c + dy[d]*s)%n

        # print(nr, nc)

        # 비 내리기
        arr[nr][nc] += 1
        bugs.add((nr, nc))

    for r, c in bugs:
        # 물이 증가한 곳 물복사 버그
        cnt = 0
        for k in (1, 3, 5, 7):
            x, y = r + dx[k], c + dy[k]
            if 0 <= x < n and 0 <= y < n and arr[x][y]:
                cnt += 1

        arr[r][c] += cnt

    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and (i, j) not in bugs:
                new.add((i, j))
                arr[i][j] -= 2

    cloud = new
answer = 0
for i in range(n):
    answer += sum(arr[i])
print(answer)