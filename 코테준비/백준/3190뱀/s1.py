dr = [-1, 0, 1, 0]      # 북 동 남 서 시계방향으로 회전
dc = [0, 1, 0, -1]

turn = {'D': 1, 'L': -1}


N = int(input())        # 격자 크기
K = int(input())        # 사과 개수
arr = [[0]*N for _ in range(N)]

for p in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1       # 사과 위치 추가

L = int(input())        # 뱀 머리의 회전 횟수
time = dict()            # [회전할 시간, 회전 방향] 담는 배열

for l in range(L):
    X, C = input().split()  # 바뀌는 시간, 방향
    time[int(X)] = C

arr[0][0] = 5     # 뱀 처음 위치 적음
idx = 1             # 처음 방향 오른쪽 - 동쪽
snake = [[0, 0], ]  # 뱀이 있는 위치를 담는 변수
result = 1          # 게임 시간 담는 변수

while True:

    r, c = snake[-1]      # 뱀 머리 위치
    sr, sc = r + dr[idx], c + dc[idx]

    if 0 <= sr < N and 0 <= sc < N and arr[sr][sc] != 5:   # 격자 안이고 몸에 부딪히지 않았다면
        snake.append([sr, sc])          # 몸통에 추가

        if arr[sr][sc] == 0:            # 아무것도 없다면
            tr, tc = snake.pop(0)
            arr[tr][tc] = 0               # 꼬리 제거

        arr[sr][sc] = 5

        if result in time.keys():      # 머리를 회전할 시간이라면
            direct = turn[time[result]]
            idx = (idx+direct)%4    # 방향 전환
        result += 1
    else:           # 격자 밖이거나 자기 몸에 부딪히면 break
        break

print(result)