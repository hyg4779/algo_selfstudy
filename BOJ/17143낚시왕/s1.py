import sys
input = sys.stdin.readline


n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]

for i in range(k):
    a, b, s, d, z = map(int, input().split())
    arr[a-1][b-1] = (s, d, z)


ans = 0
for j in range(m):

    # 해당 위치 상어 잡기
    for i in range(n):
        if arr[i][j]:
            ans += arr[i][j][2]
            arr[i][j] = 0
            break

    # 이동 된 상어 임시 배열
    new = [[0]*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if arr[r][c]:

                tmp, direct, size = arr[r][c]
                nr, nc = r, c
                speed = tmp

                '''
                상어가 이동 중 에 벽 또는 바닥 또는 수면을 찍고 되돌아 올 때
                예를 들어 4가 너비라면
                1 2 3 4 3 2  즉 (4-1)*2 만큼의 인덱스 이동이 있다
                speed만큼 이동하는데 처음 시작을 1번 째로 두고 한다면 다음 위치는 아래와 같다
                '''
                if direct == 1 or direct == 2:
                    rot = 2*(n-1)
                    if direct == 1:
                        tmp += rot-r
                    else:
                        tmp += r

                    tmp %= rot

                    if tmp >= n:
                        nr, nc, direct = rot-tmp, nc, 1
                    else:
                        nr, nc, direct = tmp, nc, 2

                else:
                    rot = 2*(m-1)
                    if direct == 4:
                        tmp += rot-c
                    else:
                        tmp += c

                    tmp %= rot

                    if tmp >= m:
                        nr, nc, direct = r, rot-tmp, 4
                    else:
                        nr, nc, direct = r, tmp, 3


            # 이미 자리에 상어가 있다면 재배치
            if new[nr][nc]:
                new[nr][nc] = max(new[nr][nc], (speed, direct, size), key=lambda x: x[2])
            else:
                new[nr][nc] = (speed, direct, size)
    # 새로 완성된 배열로 치환
    arr = new

print(ans)