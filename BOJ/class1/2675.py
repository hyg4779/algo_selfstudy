import sys
input = sys.stdin.readline

for tc in range(int(input())):
    r, word = input().split()
    r = int(r)
    for i in word:
        print(i*r, end='')
    print()