import sys
input = sys.stdin.readline

n = input()

result = sum(int(i) for i in input().strip())
print(result)