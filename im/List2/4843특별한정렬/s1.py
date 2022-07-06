import sys
sys.stdin = open('sample_input.txt')

for tc in range(int(input())):
    '''
    전략
    오름차 순으로 정렬후 새 배열에 번갈아 가며 삽입
    '''
    # 정수 개수
    N = int(input())
    # 정렬 안 된 배열
    args = list(map(int, input().split()))

    args.sort(reverse=True)
    new = [0]*N

    for i in range(0, N, 2):
        new[i], new[i+1] = args[i//2], args[-((i//2)+1)]
    result = ''

    for i in new[:10]:
        result += str(i)+ ' '

    print(f'#{tc+1} {result.strip()}')
