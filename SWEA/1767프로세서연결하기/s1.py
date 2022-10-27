import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def lining(r, c, idx, mat):
    cnt = 0

    while 0 <= r < n and 0 <= c < n:

        # 프로세서나 선에 만나면 return False
        if mat[r][c]:
            return False

        # 선그리기, 전선+1
        cnt += 1
        mat[r][c] = 1

        # 벽에 붙었다면 return True
        if r == 0 or r == n-1 or c == 0 or c == n-1:
            return [mat, cnt]

        r += direct[idx][0]
        c += direct[idx][1]


# 현재 코어번호, 현재 격자, 전선 수수
def dfs(num, arr, res, conn):
    global answer

    if num == m:

        if answer[0] < conn:
            answer = [conn, res]

        elif answer[0] == conn and answer[1] > res:
            answer[1] = res

        return

    # 현재 그릴 코어 위치
    i, j = cores[num]

    for d in range(4):
        ni, nj = i+direct[d][0], j+direct[d][1]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:

            result = lining(ni, nj, d, [row[:] for row in arr])

            # 선을 그렸다면 다음 코어 그리기
            if result:
                dfs(num+1, result[0], res+result[1], conn+1)

    dfs(num+1, arr, res, conn)


direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
T = int(input())

for tc in range(1, T+1):
    n = int(input())

    # 연결 코어수, 전선수
    answer = [0, n*n]

    cores = []
    # 첫줄 무조건 연결
    field = [list(map(int, input().split()))]

    # 둘째줄 부터 마지막-1줄 arr 추가 전 core위치 찾아서 append
    for i in range(1, n-1):
        arg = list(map(int, input().split()))
        for j in range(1, n-1):
            if arg[j]:
                cores.append((i, j))
        field.append(arg)

    # 마지막줄 무조건 연결
    field.append(list(map(int, input().split())))

    # 전선 연결해야할 코어 수
    m = len(cores)

    dfs(0, field, 0, 0)

    print(f'#{tc} {answer[1]}')