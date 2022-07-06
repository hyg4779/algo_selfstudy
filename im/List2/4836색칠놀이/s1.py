import sys
sys.stdin = open('sample_input.txt')


for tc in range(int(input())):

    matrix = [[0]*10 for _ in range(10)]
    # 칠할 영역의 수
    N = int(input())
    cnt = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):

                if matrix[r][c] == 0:
                    matrix[r][c] = color

                elif matrix[r][c] in (1, 2) and matrix[r][c] == color:
                    continue

                elif matrix[r][c] in (1, 2) and matrix[r][c] != color:
                    matrix[r][c] += color
                    cnt += 1

    print(f'#{tc+1} {cnt}')
