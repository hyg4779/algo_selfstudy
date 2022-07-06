'''
NxN 격자, 모든칸에 블록이 하나씩(검정/무지개/일반 색)
일반은 M가지 색상, 색은 M 이하의 자연수로 표현,
검정: -1, 무지개: 0
블록그룹: 연결된 블록의 집합
- 일반이 무조건 1개 이상, 일반블록의 색은 모두 같아야함
검정 미포함, 무지개는 상관없음
그룹의 블록개수는 2개이상 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 모든칸으로 이동할 수 있어야 함
기준블록: 무지개블록이 아닌 행의 번호가 가장 작은 블록, 열번호가 가장 작은 블록

오토플레이(블록그룹내)
1. 크기가 가장 큰 블록 그룹찾기 => 여러개면 무지개 블록 수가 가장 많은 => 기준 블록의 행이 가장 큰 것 => 열이 가장 큰 것
2. 1에서 찾은 그룹의 모든 블록을 제거. 개수기 B개면 B**2 점
3. 격자에 중력이 작용
4. 격자가 90도 반시계 방향으로 회전
5. 다시 중력이 작용

중력이 작용하면 검은색 블록을 제외한 모든 블록이 행 번호가 큰 칸으로 이동한다(검은색 블록은 경계 역할)
'''
from collections import deque

N, M = map(int, input().split())    # 격자 길이 / 색 개수
arr = [list(map(int, input().split())) for _ in range(N)]    # 격자

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

big = 0 # 가장 큰 블록 개수
big_rainbow = 0
big_block = []  # 가장 큰 블록 그룹



def find_stand(group):
    sr, sc = N, N
    for r, c in group:
        if arr[r][c] != 0 and r <= sr and c <= sc:
            # 1. 행번호 비교 2. 열번호 비교
            sr, sc = r, c
    return sr, sc


# 블록그룹 찾기
visit = [[0]*N for _ in range(N)]   # 방문 블록 체크

for r in range(N):
    for c in range(N):
        if 0 < arr[r][c] and visit[r][c] == 0:
            color = arr[r][c]

        cnt = 0         # 블록 그룹의 블록 개수
        rainbow = 0     # 무지개 블록 수

        queue = deque([[r, c], ])
        group = []

        while queue:    # BFS

            nr, nc = queue.popleft()    # 현재위치 담음
            visit[nr][nc] = 1     # 방문 체크
            group.append([nr, nc])
            cnt += 1

            for i in range(4):  # 4방 탐색
                nr, nc = nr + dr[i], nc + dc[i]
                if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0 and arr[nr][nc] in (0, color):

                    if arr[nr][nc] == 0:    # 무지개 블록 개수
                        rainbow += 1
                    visit[nr][nc] = 1
                    queue.append([nr, nc])
        # queue 종료

        if cnt < 2:
            continue

        if cnt > big or (cnt == big and rainbow > big_rainbow):
            big = cnt
            big_block = group

        elif cnt == big and rainbow == big_rainbow:
            br, bc = find_stand(big_block)
            cr, cc = find_stand(group)

            if br > cr or(br == cr and bc > cc):
                big_block = group

result = 0

for i, j in big_block:
    arr[i][j] = M**2
    result += 1

# B**2 점 획득
result **= 2


def gravity(mat):
    '''
    2중 for문으로는 연속적으로 빈 칸일때 무시하는 칸이 나올 수 있음
    '''
    for i in range(N-1):
        for j in range(N-1, 0, -1):
            if mat[j][i] == -1 or mat[j][i+1] == -1:
                continue
            if mat[j][i] >= 0 and mat[j][i-1] == M**2:
                mat[j][i], mat[j][i+1] = mat[j][i+1], mat[j][i]