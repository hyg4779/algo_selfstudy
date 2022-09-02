arr = [[] for _ in range(4)]
fishes = [0 for _ in range(17)]
dp = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

# 물고기 번호와 방향을 담음
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(0, 8, 2):
        arr.append([line[2*j], line[2*j+1]])
        # 물고기 번호 별 행열번호 저장
        fishes[line[2*j]] = (i, j//2)


# 상어 초기 시작
first = arr[0][0]
shark = (0, 0, first[1])
answer = first[0]
fishes[first[0]] = 0

# 0, 0 위치 초기화
arr[0][0] = -1


def move():
    # 물고기 이동
    for num in range(1, 17):
        # 먹힌 물고기는 pass
        if fishes[num] == 0:continue

        # 물고기 행, 열
        r, c = fishes[num]
        # 번호, 방향
        _, p = arr[r][c]

        # 8방향 탐색
        for d in range(8):
            # 다음 이동 방향향
            head = (p+d)%8
            nr, nc = r + dp[head][0], c + dp[head][1]

            # 이동할 수 있다면
            if 0 <= nr < 4 and 0 <= nc < 4 and arr[nr][nc] != -1:
                # 해당 위치에 물고기가 있다면
                if arr[nr][nc]:
                    # 해당 위치 물고기 번호
                    tmp = arr[nr][nc]
                    # 서로 위치 교환
                    arr[r][c], arr[nr][nc] = arr[nr][nc], (num, head)
                    # 현재 와 해당 위치 물고기의 위치 정보 수정
                    fishes[num], fishes[tmp[0]] = (nr, nc), (r, c)

                # 빈 자리라면
                else:
                    arr[r][c], arr[nr][nc] = 0, (num, head)
                    fishes[num] = (nr, nc)

                break
                # 위치 교환 했다면 브레이크
                # 위치 교환 못했다면 for문을 돌며 방향 탐색. 모든 방향 이동 불가면 제자리


def eat():
    global answer
    # 상어 이동

    x, y, s = shark
    flag = True
    while 0 <= x < 4 and 0 <= y < 4:
        x, y = x+dp[s][0], y+dp[s][1]
        if arr[x][y]:
            flag = False



move()
eat()


print(answer)