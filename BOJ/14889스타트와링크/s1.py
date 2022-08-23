'''
백준에서 맞춘 풀이와 비교 필요
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def perm(cnt, idx, start):
    global res
    if cnt == n//2:
        for i in range(n):
            if i not in start:link.append(i)

        sv, lv = 0, 0
        for i in range(n//2-1):
            for j in range(i+1, n//2):
                sv += arr[start[i]][start[j]] + arr[start[j]][start[i]]
                lv += arr[link[i]][link[j]] + arr[link[j]][link[i]]
        res = min(res, abs(sv-lv))
        link.clear()
        return

    for p in range(idx, n):
        if p in start:continue
        perm(cnt+1, idx+1, start+[p])

res = float('inf')
link = list()
perm(0, 0, [])
print(res)