from collections import defaultdict


def solution(S, C):

    # 현재 문자열 검사 함수
    def my_insert():

        checked = defaultdict(bool)
        for i in arr:
            # 알파벳일때
            if i.isalpha():
                if checked[i]:
                    return False
                checked[i] = True

            # 방해문자일때
            # 현재 열려있는 모든 문자들 초기화
            elif i == '1':
                for k in checked.keys():
                    checked[k] = False
        return True

    # 방해문자 삽입에 쉽도록 S문자열 길이를 2배로 늘림
    arr = []
    for x in S:
        arr.extend([x, '0'])

    # 방해문자 삽입 없이 가능하면 return 0
    if my_insert():
        return 0

    idx = 0
    while idx < len(C):
        # 방해문자를 넣어보며 검사

        ins = C[idx]
        arr[(ins-1)*2+1] = '1'
        idx += 1

        if my_insert():
            break
    else:
        if my_insert():
            return idx
        else:
            return -1

    return idx

print(so)