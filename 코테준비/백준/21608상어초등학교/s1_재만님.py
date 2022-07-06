N = int(input())
student = [0] * (N ** 2 + 1)            # 인덱스를 학생번호로 좋아하는 학생번호 리스트를 저장
arr = [[0] * N for _ in range(N)]       # 교실
order = []                              # 자리 정하는 학생 순서
result = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for _ in range(N ** 2):                                 # 학생 순서와 좋아하는 학생을 각각 저장
    a, b, c, d, e = list(map(int, input().split()))
    order.append(a)
    student[a] = [b, c, d, e]

for cur in order:                   # 자리정할 순서대로 순회
    x = 0                           # x, y는 현재 학생이 최종적으로 앉게 될 자리를 저장할 변수
    y = 0
    empty = -1                      # 현재 학생 자리를 순회하면서 가장 친한친구가 많은 자리의 친구 수와
    best_friend = -1                # 빈 자리수를 저장할 변수

    for r in range(N):              # 교실의 자리를 순회
        for c in range(N):
            if arr[r][c]:           # 빈자리가 아니면 다음 반복
                continue
            cur_empty = 0           # 현재 위치에서 인접한 자리의 빈자리와
            cur_best_friend = 0     # 친한친구 수를 저장할 변수

            for i in range(4):      # 4방향 탐색
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:            # 인접한 자리 중 빈자리이면
                    cur_empty += 1                                              # cur_empty를 1증가
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] in student[cur]: # 인접한 자리 중 친한친구자리이면
                    cur_best_friend += 1                                        # cur_best_friend를 1증가
            
            if cur_best_friend > best_friend:           # 현재 자리의 친한친구가 저장된 값보다 많으면
                best_friend = cur_best_friend           # 친한친구와 빈자리 모두 갱신
                empty = cur_empty
                x = r                                   # x, y도 갱신
                y = c
            
            elif cur_best_friend == best_friend and cur_empty > empty:      # 친한친구 수는 같은데 빈자리가 많은 자리이면
                empty = cur_empty                                           # 빈자리 갱신
                x = r                                                       # x, y도 갱신
                y = c
    
    arr[x][y] = cur             # 모든 자리 탐색 후 x, y 자리를 현재 학생 자리로 선정

for r in range(N):              # 다시 교실 자리 순회
    for c in range(N):
        cnt = 0                 # 인접 자리의 친한친구 수를 저장할 변수
        for i in range(4):      # 4방향 탐색
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] in student[arr[r][c]]:       # 인접자리가 친한친구이면 cnt +1
                cnt += 1
        
        if cnt:                             # 만약 cnt가 있으면
            result += 10 ** (cnt - 1)       # 문제의 조건대로 점수를 추가

print(result)
