import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(idx, cnt):
    global answer, number

    # 횟수를 채웠다면 최댓값 갱신
    if cnt == turn:
        answer = max(answer, int(''.join(number)))
        return

    # 숫자를 돌면서 앞보다 큰 뒤에 숫자 발견시 바꾸고 dfs
    for i in range(idx, n-1):
        for j in range(i+1, n):
            if number[i] <= number[j]:
                number[i], number[j] = number[j], number[i]
                dfs(i, cnt+1)
                number[i], number[j] = number[j], number[i]

    # dfs를 돌아도 갱신이 안됐고, 교환횟수를 채우지 못했다면
    # 남은 교환횟수
    # 홀수: 끝에 두자리 바꾸고 마무리 / 짝수: 그대로
    if not answer and cnt < turn:
        rotate = (turn - cnt)%2
        if rotate:
            number[-1], number[-2] = number[-2], number[-1]
        dfs(idx, turn)


T = int(input())
for tc in range(1, T+1):
    # 숫자, 횟수
    number, turn = input().split()
    n = len(number)

    turn = int(turn)

    number = list(number)
    answer = 0
    dfs(0, 0)

    print(f'#{tc} {answer}')