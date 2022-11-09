import heapq

def solution(n, student, point):
    answer = -1

    # 열반 번호
    prime = set([i for i in range(n//2, n)])

    # 전체 학생 점수
    info = [[0, i] for i in range(n)]

    for num, score in zip(student, point):
        info[num-1][0] += score

        # 새 열반 점수, 번호 번호
        new = set()
        regen = []
        for j in range(n//2):
            tmp = heapq.heappop(info)

            # 전체 학생에서 점수순으로 절반만 빼서 tmp에 담음
            new.add(tmp[1])
            regen.append(tmp)

        info.extend(regen)

        if new != prime:
            answer += 1
            prime = new

    return answer


print(solution(6, [6, 1, 4, 2, 5, 1, 3, 3, 1, 6, 5], [3, 2, 5, 3, 4, 2, 4, 2, 3, 2, 2]))
print(solution(10, [3, 2, 10, 2, 8, 3, 9, 6, 1, 2], [3, 2, 2, 5, 4, 1, 2, 1, 3, 3]))