'''
0. new는 S+N 으로 나뉘어 있고
    1) S는 소문자 a-z 3이상 6이하 길이
    2) N은 숫자. 길이는 0에서 6이하, 첫 시작 0일 수 없음
1. new가 regi에 없다면 추천하고 종료
2. regi에 있다면
    1) 뒤 숫자열 부분을 +1해서 1로 복귀
'''
def solution(registered_list, new_id):
    answer = ''
    n, m = len(registered_list), len(new_id)
    checked = [0]*n

    if new_id not in registered_list:
        return new_id
    else:
        S, N = '', ''
        # S, N 나누기
        for i in range(m):
            if new_id[i].isdigit():
                S, N = new_id[:i], new_id[i:]
                break
        else:
            S, N = new_id, ''


