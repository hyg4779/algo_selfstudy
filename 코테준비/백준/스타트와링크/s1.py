import sys
sys.stdin = open('input.txt')


def perm(n, group):
    global min_v
    if group in memo:     # 인원수가 절반이고 했던 조합이 아니라면
        return

    elif n==N//2 and group not in memo:
        memo.append(group[::])                     # 조합 추가

        # 링크 팀짜기 시작
        link = [-1]*(N//2)   # 링크 팀
        n = 0                   # 링크 팀 인원수
        for i in range(N):
            if n == N//2:       # 팀 인원수 절반 채웠으면 멈춤
                break
            if i in group:      # 스타팀에 있는 선수는 제외
                continue
            link[n] = i
            n += 1
        memo.append(link[::])
        # 각 팀 능력치 계산
        sv = 0
        lv = 0
        for i in range(N//2-1):
            for j in range(i+1, N//2):
                if abs(sv-lv) > min_v:
                    return
                sv += arr[group[i]][group[j]] + arr[group[j]][group[i]]
                lv += arr[link[i]][link[j]] + arr[link[j]][link[i]]

        if min_v > abs(sv-lv):
            min_v = abs(sv-lv)
        return

    for i in range(N):
        if i in group:
            continue
        group[n] = i
        perm(n + 1, group)
        group[n] = -1


N = int(input())    # 축구하러 모인 인원
arr = [list(map(int, input().split())) for _ in range(N)]   # 능력치 배열 arr[i][i] = 0


memo = list()       # 했던 조합들은 다시 계산하지 않기 위해 만든 변수
members = [-1]*(N//2)
min_v = 100*(N//2)

perm(0, members)
print(min_v)

############################################################################

def perm(n):
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

    for i in range(N):
        if i in start:continue
        if len(start) > 0 and start[len(start)-1] > i:continue
        start.append(i)
        perm(n + 1)
        start.pop()


N = int(input())    # 축구하러 모인 인원
arr = [list(map(int, input().split())) for _ in range(N)]   # 능력치 배열 arr[i][i] = 0


start = []
link = []
min_v = float('Inf')

perm(0)
print(min_v)