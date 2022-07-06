import sys
sys.stdin = open('sample_input.txt')


def palindrome(mat, n, l):

    for i in range(n):
        tmp = mat[i]
        ver = ''
        for j in range(n):
            ver += mat[j][i]

        for idx in range(0, n-l+1):
            horz = tmp[idx:idx+l]
            vert = ver[idx:idx+l]

            if horz == horz[::-1]:
                return horz
            if vert == vert[::-1]:
                return vert



for tc in range(int(input())):
    # NxN 글자판 M길이의 회문
    N, M = map(int, input().split())

    matrix = [input() for _ in range(N)]
    print(f'#{tc+1} {palindrome(matrix, N, M)}')


    '''
    행열전환
    list(map(''.join, zip(*mnm)))
    '''