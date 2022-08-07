def solution(param):
    tmp = param**0.5
    if tmp**4 == float(param)**2:
        return int((tmp+1)**2)
    return -1