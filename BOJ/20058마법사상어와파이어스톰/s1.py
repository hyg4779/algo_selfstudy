import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
N = 2**N
arr = [list(map(int, input().split())) for _ in range(N)]

L = list(map(int, input().split()))
rot = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for q in L:
    size = 2**q
    for r in range(0, N, 2):
        for c in range(0, N, 2):
            tmp, idx, p = arr[r][c], 0, 0
            while idx < 4:
                p += 1
                if p==size:
                    idx += 1
                    p = 1
                    continue
                sr, sc = r+rot[idx][0]*p, c+rot[idx][1]*p
                tmp, arr[sr][sc] = arr[sr][sc], tmp
