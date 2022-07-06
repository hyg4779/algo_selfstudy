import sys
sys.stdin = open('sample_input.txt')


def part_sum(n, k):
    # 1 부터 12까지를 원소로 갖는 집합 생성
    arr = [num for num in range(1, 13)]

    # arr의 원소 개수
    arr_parts = len(arr)

    # 모든 부분집합을 담을 list 생성
    set_list = []

    for i in range(1 << arr_parts):

        # i를 원소로 갖는 부분집합을 담을 list
        sub_list = []

        for j in range(arr_parts + 1):
            if i & (1 << j): # i의 j 번째 비트가 1이면

                sub_list.append(arr[j])
        set_list.append(sub_list)

    # 부분집합의 개수가 N과 같고 합이 K와 같은 함수의 개수 담는 변수
    result = 0

    for i in set_list:
        if len(i) == n:
            if sum(i) == k:
                result += 1

    return result


for tc in range(1, int(input())):
    N, K = map(int, input().split())

    print('#{} {}'.format(tc, part_sum(N, K)))