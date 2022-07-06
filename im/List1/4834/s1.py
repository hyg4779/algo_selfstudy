import sys
sys.stdin = open('sample_input.txt')



for tc in range(int(input())):
    N = int(input())
    args = list(input())
    counts = dict()
    for i in args:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1

    # print(counts)
    tmp_i = 0
    tmp_c = 0
    for j in counts:
        if tmp_c == counts[j] and tmp_i < j:
            tmp_i = j
        elif counts[j] > tmp_c:
            tmp_c = counts[j]
            tmp_i = j
    print(f'#{tc+1} {tmp_i} {tmp_c}')