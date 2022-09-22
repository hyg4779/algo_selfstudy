from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
rr, rc = 0, 0
br, bc = 0, 0

for i in range(1, n-1):
    for j in range(1, m-1):
        if field[i][j] == 'R':
            rr, rc = i, j
        elif field[i][j] == 'B':
            br, bc = i, j

visit = [[[[-1]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
visit[rr][rc][br][bc] = 0

Q = deque([(rr, rc, br, bc)])

while Q:
    ri, rj, bi, bj = Q.popleft()

    if field[ri][rj] == 'O':
        print(visit[ri][rj][bi][bj])
        exit()

    if visit[ri][rj][bi][bj] >= 10:
        continue

    for d in direct:
        # 빨간 구슬 이동
        nri, nrj = ri, rj
        while True:
            nri += d[0]
            nrj += d[1]
            if field[nri][nrj] == '#':
                nri -= d[0]
                nrj -= d[1]
                break
            if field[nri][nrj] == 'O':
                break

        # 파란 구슬 이동
        nbi, nbj = bi, bj
        while True:
            nbi += d[0]
            nbj += d[1]
            if field[nbi][nbj] == '#':
                nbi -= d[0]
                nbj -= d[1]
                break
            if field[nbi][nbj] == 'O':
                break

        # 파란 구슬이 구멍에 빠지면 continue
        if field[nbi][nbj] == 'O':
            continue

        # 두개 위치가 같다면 늦게 이동한 구슬이 한칸 뒤로 이동
        if nri == nbi and nrj == nbj:
            if abs(nri - ri) + abs(nrj - rj) > abs(nbi - bi) + abs(nbj - bj):
                nri -= d[0]
                nrj -= d[1]
            else:
                nbi -= d[0]
                nbj -= d[1]

        if visit[nri][nrj][nbi][nbj] == -1:
            visit[nri][nrj][nbi][nbj] = visit[ri][rj][bi][bj] + 1
            Q.append((nri, nrj, nbi, nbj))
else:
    print(-1)