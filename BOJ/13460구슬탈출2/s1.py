from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
red, blue, hole = [0, 0], [0, 0], [0, 0]

for a in range(1, n-1):
    for b in range(1, m-1):
        if arr[a][b]=='R':
            red = [a, b]
        elif arr[a][b]=='B':
            blue = [a, b]
        elif arr[a][b]=='O':
            hole = [a, b]

Q = deque([(red[0], red[1], blue[0], blue[1], 0)])

while Q:
    rr, rc, br, bc, cnt = Q.popleft()

    for d in direct:
        p = 1
        x, y = rr+d[0]*p, rc+d[1]*p
        while 0 < x < n-1 and 0 < y < m-1 and arr[x][y] != '#':
            if [x, y] == hole:
                break
            p += 1
            x, y = rr+d[0]*p, rc+d[1]*p

        if p != 1:
            rr, rc = x, y

        p = 1
        x, y = br+d[0]*p, bc+d[1]*p
        while 0 < x < n-1 and 0 < y < m-1 and arr[x][y] != '#':
            if [x, y] == hole:
                break
            p += 1
        if p != 1:
            br, bc = x, y
