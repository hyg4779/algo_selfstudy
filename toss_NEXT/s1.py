def solution(arr):

    rect = [[], [], [], []]         # 왼쪽 위, 오른쪽 위 왼쪽 아래, 오른쪽 아래
    i, h = float('inf'), 0          # 가장 상단 횡, 가장 하단 횡
    j, v = float('inf'), 0          # 가장 좌측 열, 가장 우측 열

    for r, c in arr:
        i, h = min(i, r), max(h, r)
        j, v = min(j, c), max(v, c)

    for r, c in arr:
        if r == i and c == j:           # 왼쪽 꼭지점과 같다면
            rect[0] = [r, c]
        elif r == i and c == v:
            rect[1] = [r, c]
        elif r == h and c == j:
            rect[2] = [r, c]
        else:
            rect[3] = [r, c]

    for now in range(4):
        if not rect[now]:
            if now == 0:
                return [i, j]
            elif now == 1:
                return [i, v]
            elif now == 2:
                return [h, j]
            else:
                return [h, c]


print(solution([[1, 4], [3, 4], [3, 10]]))
print(solution([[1, 1], [2, 2], [1, 2]]))