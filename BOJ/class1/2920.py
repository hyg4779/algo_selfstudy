import sys
input = sys.stdin.readline

line = list(map(int, input().split()))

result = 'descending' if line[0] > line[1] else 'ascending'

for i in range(2, 8):
    n = line[i-1] - line[i]
    if n > 0:
        if result == 'ascending':
            print('mixed')
            exit()
    else:
        if result == 'descending':
            print('mixed')
            exit()
print(result)