def perm(n, s):
    global min_v

    if n == N//2:
        # 각 팀 능력치 계산
        sv = 0
        lv = 0

        for i in range(N):
            if i in start:
                continue
            link.append(i)

        for i in range(N//2-1):
            for j in range(i+1, N//2):

                sv += arr[start[i]][start[j]] + arr[start[j]][start[i]]
                lv += arr[link[i]][link[j]] + arr[link[j]][link[i]]

        if min_v > abs(sv-lv):
            min_v = abs(sv-lv)
        link.clear()
        return

    for i in range(s, N):
        if i in start:continue
        start.append(i)
        perm(n + 1, s+1)
        start.pop()


N = int(input())    # 축구하러 모인 인원
arr = [list(map(int, input().split())) for _ in range(N)]   # 능력치 배열 arr[i][i] = 0


start = []
link = []
min_v = float('Inf')

perm(0, 0)
print(min_v)