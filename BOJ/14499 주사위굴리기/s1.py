import sys
input = sys.stdin.readline


n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
comm = list(map(int, input().split()))

dice = [0 for _ in range(7)]
direct = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]


for i in comm:
    d = direct[i]
    nx, ny = x+d[0], y+d[1]
    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny

        if i == 1:
            dice[1], dice[4], dice[6], dice[3] = dice[4], dice[6], dice[3], dice[1]
        elif i == 2:
            dice[1], dice[4], dice[6], dice[3] = dice[3], dice[1], dice[4], dice[6]
        elif i == 3:
            dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]
        else:
            dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]

        if arr[x][y]==0:
            arr[x][y] = dice[6]
        else:
            dice[6] = arr[x][y]
            arr[x][y] = 0

        print(dice[1])
