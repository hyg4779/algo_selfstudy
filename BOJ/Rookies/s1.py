'''
정렬된 스텍3개
4번째 스텍으로 옮기는 것 내림차순 정렬로
'''

def solution(stack1, stack2, stack3):
    # return array
    answer = []

    # 스택별 숫자가 등장한 스텍 번호를 적을 배열
    nums = ['' for _ in range(1001)]

    # 스텍들의 숫자를 nums배열에 적는 함수
    def move(stack: list, idx: str) -> None:
        for num in stack:
            nums[num] = idx
        pass


    move(stack1, '1')
    move(stack2, '2')
    move(stack3, '3')

    # nums를 돌며 등장한 숫자의 위치를 answer에 추가
    for i in range(1000, -1 , -1):
        if nums[i]:
            answer.append(nums[i])
    return ''.join(answer)

print(solution([2, 7], [4, 5], [1]))
print(solution([10, 20, 30], [8], [1]))
print(solution([7], [], [9]))
