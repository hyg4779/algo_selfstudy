N = int(input())

stu = [[0] for _ in range(N**2+1)]
order = []
for i in range(N**2):
    # 학생번호, 좋아하는 학생 번호
    num, a, b, c, d = map(int, input().split())

    order.append(num)
    stu[num] = [a, b, c, d]

room = [[0]*N for _ in range(N)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for o in order:
    x = 0
    y = 0
    blank = -1
    like = -1

    for r in range(N):
        for c in range(N):
            if room[r][c]:
                continue
            cur_blank = 0
            cur_like = 0
            for idx in range(4):
                i = r + di[idx]
                j = c + dj[idx]

                if 0 <= i < N and 0 <= j < N:
                    if room[i][j] == 0:
                        cur_blank += 1
                    if room[i][j] in stu[o]:
                        cur_like += 1

            if cur_like > like:
                like = cur_like
                blank = cur_blank
                x = r
                y = c
            elif cur_like == like and cur_blank > blank:
                blank = cur_blank
                x = r
                y = c

    room[x][y] = o

result = 0
for r in range(N):
    for c in range(N):
        cnt = 0
        for idx in range(4):      # 4방향 탐색
            i = r + di[idx]
            j = c + dj[idx]

            if 0 <= i < N and 0 <= j < N and room[i][j] in stu[room[r][c]]:
                cnt += 1

        if cnt:
            result += 10 ** (cnt -1)
print(result)