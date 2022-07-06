import sys
sys.stdin = open('sample_input.txt')


for tc in range(int(input())):
    '''
    K: 한번 충전 이동할 수 있는 정류장 수
    N: 0번 부터 종점 N번 정류장
    M: 충전기가 설치된 M개의 정류장
    '''
    K, N, M = map(int, input().split())
    # 충전소가 있는 정류장 번호
    charges = list(map(int, input().split()))

    cnt = 0
    bus = 0
    tmp = K
    while tmp:

        if bus + tmp in charges:
            bus += tmp
            tmp = K
            cnt += 1

        elif bus + tmp >= N:
            print(f'#{tc+1} {cnt}')
            break

        else:
            tmp -= 1

    else:
        if tmp == 0:
            print(f'#{tc+1} 0')