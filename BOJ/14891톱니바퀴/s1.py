from collections import deque
import sys
read = sys.stdin.readline

'''
톱니 끼리 맞닿는 부분은 총 3곳
1-2 , 2-3, 3-4
각각 톱니들이 맞닿는 부분의 위치
1-2: 2-6
2-3: 2-6
3-4: 2-6

n번의 톱니가 회전을 할 때,
1) 첫 톱니 회전
2) 맞닿은 톱니들 확인
    1. 회전 전 다른 극이면 회전
        1) 주변 톱니 회전
    2. 회전 전 다른 극이 아니 었다면 정지
        1) 주변 톱니 회전 안함
3) 모든 톱니 회전 후
    1. 회전한 방향들 따라 톱니 회전
    2. 톱니들 맞닿은 부분들 check
'''

# 톱니 4개 정보
wheels = [0] + [read().rstrip() for _ in range(4)]

# 회전 횟수
k = int(read())

# 처음 톱니의 맞닿은 곳인지 배열
info = [0,
        # 1번 톱니
        [-1, False if wheels[1][2] == wheels[2][6] else True],
        # 2번 톱니
        [False if wheels[1][2] == wheels[2][6] else True, False if wheels[2][2] == wheels[3][6] else True],
        # 3번 톱니
        [False if wheels[2][2] == wheels[3][6] else True, False if wheels[3][2] == wheels[4][6] else True],
        # 4번 톱니
        [False if wheels[3][2] == wheels[4][6] else True, -1]
        ]


# 톱니 별 좌 우 톱니들과 맞닿았는지 True, False 배열
def check():
    for i in range(1, 5):
        for j in range(2):
            # 맞닿은 부분이 없다면 continue
            if info[i][j] == -1:continue

            # 왼쪽에 닿은 톱니
            if j == 0:
                info[i][j] = False if wheels[i-1][2] == wheels[i][6] else True

            # 오른쪽에 닿은 톱니
            elif j == 1:
                info[i][j] = False if wheels[i][2] == wheels[i+1][6] else True


def turn():
    for i in range(1, 5):
        # 시계방향 회전
        if visit[i] == 1:
            wheels[i] = wheels[i][-1]+wheels[i][:7]

        # 반시계 방향 회전
        elif visit[i] == -1:
            wheels[i] = wheels[i][1:]+wheels[i][0]


for _ in range(k):
    wheel, d = map(int, read().split())
    visit = [0]*5
    visit[wheel] = d

    # 회전할 톱니 번호와 방향을 담을 큐
    Q = deque([])

    if wheel-1 >= 1:
        # 톱니가 서로 다른 극으로 맞닿아 있다면
        if info[wheel-1][1]:
            # 톱니 번호와 회전할 방향을 담아서 append
            Q.append((wheel-1, -d))
    if wheel+1 <= 4:
        if info[wheel+1][0]:
            Q.append((wheel+1, -d))

    while Q:
        # 번호와 방향
        now, direct = Q.popleft()

        # 회전 방향 담음
        visit[now] = direct

        if now-1 >= 1:
            # 톱니가 서로 다른 극으로 맞닿아 있다면
            if info[now-1][1] and visit[now-1]==0:
                # 톱니 번호와 회전할 방향을 담아서 append
                Q.append((now-1, -direct))
        if now+1 <= 4:
            if info[now+1][0] and visit[now+1]==0:
                Q.append((now+1, -direct))

    turn()
    check()

answer = 0
for num in range(1, 5):
    if wheels[num][0] == '1':
        answer += 2**(num-1)
print(answer)