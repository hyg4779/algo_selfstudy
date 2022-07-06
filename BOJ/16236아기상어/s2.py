N = int(input())        # 격자 크기
arr = [list(map(int, input().slpit())) for _ in range(N)]   # 격자

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
babe = ()
fishes = []

for a in range(N):
    for b in range(N):
        if 0 < arr[a][b] < 9:
            fishes.append((a, b))

        elif arr[a][b] == 9:
            babe = (a, b)
            arr[a][b] = 0