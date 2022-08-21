from collections import deque
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    home = list(map(int, input().split()))
    graph = [list(map(int, input().split())) for _ in range(n)]
    fest = list(map(int, input().split()))

    visit = [0]*(n+1)

