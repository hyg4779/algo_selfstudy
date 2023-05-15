import sys
input = sys.stdin.readline

n, x = input().split()
print(*filter(lambda y: y < int(x), map(int, input().split())))