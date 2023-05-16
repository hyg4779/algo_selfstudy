import sys
input = sys.stdin.readline

n, m = map(int, input().split())
print('>') if n > m else print('==') if n == m else print('<')