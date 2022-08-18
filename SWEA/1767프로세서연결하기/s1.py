from copy import deepcopy as dc
from collections import deque
import sys
input = sys.stdin.readline

direct = [(0, 1), (1, 0), (-1, 0), (-1, 0)]
sys.argv
def dfs(now, s, cnt):
    global mincodes

    if s == len(sensor):
        mincodes = min(mincodes, cnt)

    for i in range(s, len(sensor)):
        r, c = sensor[i]
        for d in direct:

            for p in range(1, n):
                sr, sc = r+d[0]*p, d+d[1]*p
                if 0 <= sr < n and 0 <= sc < n:
                    if arr[sr][sc]:break

for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    sensor = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            if arr[i][j]:sensor.append((i, j))


    answer = 12*n


