def solution(triangle):
    n = len(triangle)

    for i in range(n-2, -1, -1):
        for j in range(1, i+2):
            triangle[i][j-1] += max(triangle[i+1][j-1], triangle[i+1][j])
    return triangle[0][0]


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))