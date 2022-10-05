# 참고: https://baby-ohgu.tistory.com/3
import sys
input = sys.stdin.readline

def check():
    for start in range(n):
        k = start
        # 가로선 이동
        for j in range(h):
            # 가로선이 존재한다면
            if field[j][k]:
                k += 1
            # 왼쪽에 가로선이 있다면
            elif k > 0 and field[j][k-1]:
                k -= 1

        # 가장 하단까지 왔는데 k가 start랑 같지 안흥면 정상 도착하지 않는 것이므로 return False
        if k != start:
            return False
    return True


def dfs(cnt, x, y):
    global answer
    # 현재 상태에서 각 출발점이 도착점으로 잘 도착하는지 확인
    if check():
        answer = min(answer, cnt)
        return

    # 도착점이 정상적이지 않고, 3개의 다리를 놓았거나, 현재 값보다 많은 다리를 놓은 경우라면 return
    elif cnt == 3 or answer <= cnt:
        return

    for i in range(x, h):
        # 가로선을 우선 탐색

        # 행이 변경되기 전에는 가로선을 계속해서 탐색
        if i == x:
            k = y
        # 행이 변경될 경우 가로선 처음부터 탐색
        else:
            k = 0

        for j in range(k, n-1):
            # 가로선을 놨을 때 오른쪽에 다리가 존재하지 않는 경우
            if not field[i][j] and not field[i][j+1]:

                # 가로선을 놨을 때 왼쪽에 -가 존재하면 연속된 가로선이므로 continue
                if j > 0 and field[i][j-1]:
                    continue

                field[i][j] = True
                # cnt 1증가, 세로선 그대로, 가로선 두칸 이동
                dfs(cnt+1, i, j+2)
                field[i][j] = False


n, m, h = map(int, input().rstrip().split())
# 특정 지점 방문 여부 체크
field = [[False]*n for _ in range(h)]

# 출발점에서 바로 도착점으로 내려오므료 0출력 후 종료
if m == 0:
    print(0)
    exit()

for _ in range(m):
    a, b = map(int, input().split())
    field[a-1][b-1] = True

# 결괏값
answer = 4
dfs(0, 0, 0)
print(answer if answer < 4 else -1)
