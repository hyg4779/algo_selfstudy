from collections import deque

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]


def indexing():
    dr, dc = [0, 1, 0, -1], [-1, 0, 1, 0]
    r, c = n//2, n//2
    depth = 0
    snail = []
    while True:
        for i in range(4):
            if i%2 == 0:
                depth += 1
            for j in range(depth):
                r, c = r + dr[i], c + dc[i]
                snail.append((r, c))
                if r == 0 and c == 0:
                    return snail


def magic(d, s):
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    r, c = n//2, n//2

    for _ in range(s):
        r, c = r + dr[d], c + dc[d]
        if 0 <= r < n and 0 <= c < n:
            field[r][c] = 0
        else:
            break

    move()
    while bomb():
        move()

    duplicate()


def move():
    blank = deque([])

    for r, c in snail:
        # 빈칸이면 담음
        if field[r][c] == 0:
            blank.append((r, c))

        # 빈칸이 아니고 이전에 빈칸들이 있었다면 당김
        elif blank:
            i, j = blank.popleft()
            field[i][j] = field[r][c]
            field[r][c] = 0
            blank.append((r, c))


def bomb():
    num, cnt = -1, 0
    visit = deque()
    flag = False
    for r, c in snail:
        # 지금 구슬과 이전 구슬이 같다면
        if field[r][c] == num:
            visit.append((r, c))
            cnt += 1

        # 다르다면
        else:
            if cnt >= 4:
                answer[num-1] += cnt
                flag = True

            while visit:
                i, j = visit.popleft()
                if cnt >= 4:
                    field[i][j] = 0

            num = field[r][c]
            cnt = 1
            visit.append((r, c))

    return flag


def duplicate():
    new = []
    i, j = snail[0]
    now, cnt = field[i][j], 1

    for r, c, in snail[1:]:
        if field[r][c] == now:
            cnt += 1

        elif field[r][c]:
            new.extend([cnt, now])
            now = field[r][c]
            cnt = 1

    idx = 0
    for r, c in snail:
        if not new:
            break

        field[r][c] = new[idx]
        idx += 1
        if idx >= len(new):
            break
    pass




snail = indexing()
answer = [0]*3
print(snail)

for _ in range(m):
    d, s = map(int, input().split())
    magic(d-1, s)
result = 0
for i in range(3):
    result += answer[i]*(i+1)

print(result)