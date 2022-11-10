from collections import deque


# 상어 위치부터 바깥으로 뻗어 나가는 인덱스
def snailing():
    indexing = []
    depth = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    x, y = n//2, n//2

    while True:
        for i in range(4):
            if i%2 == 0:
                depth += 1
            for j in range(depth):
                x += dx[i]
                y += dy[i]
                indexing.append((x, y))
                if x == 0 and y == 0:
                    return indexing


# 마법
def blizard(idx, dist):
    x, y = n//2, n//2
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(dist):
        x += dx[idx]
        y += dy[idx]
        if 0 <= x < n and 0 <= y < n:
            arr[x][y] = 0

        else:
            break

    filling()
    while bomb():
        filling()
    grouping()


# 빈자리 채우기
def filling():
    blanks = deque([])

    for x, y in snail:
        if arr[x][y] == 0:
            blanks.append((x, y))

        elif arr[x][y] and blanks:
            nx, ny = blanks.popleft()
            arr[nx][ny] = arr[x][y]
            arr[x][y] = 0
            blanks.append((x, y))


# 같은숫자 4칸 연속 > 터뜨리기
def bomb():
    visit = deque([])
    cnt = 0
    num = -1
    flag = False

    for x, y in snail:
        if num == arr[x][y]:
            visit.append((x, y))
            cnt += 1

        else:
            if cnt >= 4:
                score[num-1] += cnt
                flag = True

            while visit:
                nx, ny = visit.popleft()
                if cnt >= 4:
                    arr[nx][ny] = 0

            num = arr[x][y]
            cnt = 1
            visit.append((x, y))

    return flag


# 복제 마법
def grouping():
    cnt = 1
    tmpx, tmpy = snail[0]
    num = arr[tmpx][tmpy]
    nums = []

    for i in range(1, len(snail)):
        x, y = snail[i]
        if num == arr[x][y]:
            cnt += 1

        else:
            nums.append(cnt)
            nums.append(num)
            num = arr[x][y]
            cnt = 1

    idx = 0
    for x, y in snail:
        if not nums:
            break

        arr[x][y] = nums[idx]
        idx += 1
        if idx == len(nums):
            break


# 격자크기, 마법횟수
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

snail = snailing()
score = [0]*3

for _ in range(m):
    d, s = map(int, input().split())
    blizard(d-1, s)


answer = 0
for i in range(3):
    answer += (i+1)*score[i]


print(answer)
