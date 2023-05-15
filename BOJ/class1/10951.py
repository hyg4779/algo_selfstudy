import sys
lines = sys.stdin.readlines()

for line in lines:
    n, m = map(int, line.split())
    print(n + m)

'''
while True:
    try:
        A, B = map(int, input().split())
    except EOFError:
        break
'''