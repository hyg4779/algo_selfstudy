import sys
sys.stdin = open('sample_input.txt')


def binarysearch(pages, target):
    start = 1
    end = pages

    mid = (start + end)//2

    # 탐색 횟 수
    cnt = 0

    while start <= end:
        cnt += 1
        if mid == target:
            return cnt

        if mid > target:
            end = mid - 1

        elif mid < target:
            start = mid + 1

        mid = (start + end)//2

    return 0

for tc in range(int(input())):
    # 전체 쪽 수, 찾아야 하는 쪽 번호
    P, A, B = map(int, input().split())

    A_cnt = binarysearch(P, A)
    B_cnt = binarysearch(P, B)

    if A_cnt < B_cnt:
        result = 'A'
    elif A_cnt > B_cnt:
        result = 'B'
    else:
        result = 0

    print(f'#{tc+1} {result}')
