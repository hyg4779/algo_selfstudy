import sys
input = sys.stdin.readline

val, idx = -1 , -1

for i in range(1, 10):
    n = int(input())
    if val < n:
        val, idx = n, i

print(f'{val}\n{idx}')
