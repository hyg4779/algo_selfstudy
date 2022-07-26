from collections import deque

def solution(maps):
    answer = float('inf')

    n, m = len(maps), len(maps[0])
    direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    visit = [[0]*m for _ in range(n)]
    visit[0][0] = 1
    Q = deque([(1, 0, 0)])
    while Q:
        cnt, r, c = Q.popleft()

        if r==n-1 and c==m-1:
            answer = min(answer, cnt)
            continue

        for d in direct:
            sr, sc = r+d[0], c+d[1]
            if 0 <= sr < n and 0 <= sc < m and maps[sr][sc] and not visit[sr][sc]:
                visit[sr][sc] = 1
                Q.append((cnt+1, sr, sc))

    if answer==float('inf'):
        return -1
    return answer