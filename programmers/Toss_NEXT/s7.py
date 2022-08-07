from itertools import combinations


def solution(n):
    answer = 0

    items = list(range(1, n+1))
    for num in range(1, n+1):
        tmp = list(combinations(items, num))

        for i in range(len(tmp)):
            now = tmp[i]
            flag = False




    return answer

print(solution(3))