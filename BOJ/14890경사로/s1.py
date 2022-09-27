import sys
input = sys.stdin.readline

# 경사로 설치했을 때, 지나갈 수 있다면 True, 없으면 False를 return
def check(line):
    sw = [False for i in range(n)]
    for idx in range(n-1):
        # 현재 칸, 다음 칸 높이 같다면 continue
        if line[idx] == line[idx+1]:
            continue

        # 현재 칸 다음 칸 높이차이 1 이상이면 return False
        if abs(line[idx]-line[idx+1]) > 1:
            return False

        # 현재 칸이 다음 칸 보다 높다면
        if line[idx] > line[idx+1]:
            # 다음 칸(낮은 칸)의 높이
            tmp = line[idx+1]
            # 낮은 칸부터 경사로의 길이만큼 탐색하면서
            for j in range(idx + 1, idx + 1 + l):

                # 격자 크기 내
                if j < n:

                    # 크기가 달려지면 return Fasle
                    if line[j] != tmp: return False

                    # 이미 경사로가 놓인 곳이면 return False
                    if sw[j] == True: return False

                    # 경사로 설치
                    sw[j] = True

                # 격자 밖이면 return False
                else:
                    return False

        # 현재 칸이 다음 칸보다 낮다면
        else:
            tmp = line[idx]
            for j in range(idx, idx-l, -1):
                if 0 <= j:
                    if line[j] != tmp: return False
                    if sw[j] == True: return False
                    sw[j] = True
                else:
                    return False

    # 경사로 설치가 끝났다면
    return True


n, l = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in field:
    # 행탐색 하며 지나갈 수 있는 길이면 cnt+1
    if check(i):
        cnt += 1

for i in range(n):
    tmp = []
    # 탐색할 열을 행으로 바꿔서 탐색, 지나갈 수 있다면 cnt+1
    for j in range(n):
        tmp.append(field[j][i])

    if check(tmp):
        cnt += 1

print(cnt)