def solution(arr):
    answer = True

    for i in range(9):
        r_cnt, c_cnt = [0]*10, [0]*10
        for j in range(9):
            r_cnt[arr[i][j]] = 1
            c_cnt[arr[j][i]] = 1

        for idx in range(1, 10):
            if r_cnt[idx] != 1 or c_cnt[idx] != 1:
                return False

    for r in range(0, 9, 3):
        r_cnt, c_cnt = [0]*10, [0]*10
        for c in range(0, 9, 3):
            for v in range(3):
                for h in range(3):
                    r_cnt[arr[r+v][c+h]] = 1
                    c_cnt[arr[c+h][r+v]] = 1

            for idx in range(1, 10):
                if r_cnt[idx] != 1 or c_cnt[idx] != 1:
                    return False

    return answer