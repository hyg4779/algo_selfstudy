def solution(n, student, point):
    answer = 0

    # 학생들 점수 정보
    info = [[0, i] for i in range(n+1)]

    prime = [row[:] for row in info[1:1+n//2]]

    return answer


# 7
print(solution(6, [6, 1, 4, 2, 5, 1, 3, 3, 1, 6, 5], [3, 2, 5, 3, 4, 2, 4, 2, 3, 2, 2]))
# 4
# print(solution(10, [3, 2, 10, 2, 8, 3, 9, 6, 1, 2], [3, 2, 2, 5, 4, 1, 2, 1, 3, 3]))