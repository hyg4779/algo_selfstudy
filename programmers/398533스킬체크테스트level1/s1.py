def solution(n, lost, reserve):
    l = len(lost)
    for i in range(1, n+1):

        if i in lost and i in reserve:
            reserve.pop(reserve.index(i))
            lost.pop(lost.index(i))
            l -= 1

    lost = set(lost)
    reserve = set(reserve)

    for i in lost:
        if i-1 in reserve:
            l -= 1
            reserve -= {i-1}
        elif  i+1 in reserve:
            l -= 1
            reserve -= {i+1}

    return n-l