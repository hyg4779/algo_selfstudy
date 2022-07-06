import sys
sys.stdin = open('input.txt')

def visor(n):   # 감시해야할 학생 수
    if n <= 0:
        return 1

    sub = n//C
    if sub:
        n -= C*sub

    if n:
        sub += 1
    return sub + 1


N = int(input())        # 시험장 수
arr = input()           # 시험장 별 응시인원

if len(arr) >= 2:       # 시험장 수가 2개 이상일 때
    arr = list(map(int, arr.split()))
else:                   # 시험장 수가 1개라면
    arr = [int(arr)]

B, C = map(int, input().split())    # 총, 부 가능 감시인원
result = 0      # 필요한 감독관 수

for i in range(N):
    result += visor(arr[i]-B)

print(result)