import sys
sys.stdin = open('sample_input.txt')


for tc in range(int(input())):
    wrd = input()
    txt = input()

    N = len(wrd)

    result = 0

    wrd_dict = {wrd[i]: N-i-1 for i in range(N)}

    idx = N-1
    while idx < len(txt):
        j = N-1

        while j >= 0:
            if txt[idx] == wrd[j]:
                idx -= 1
                j -= 1
            else:
                break

        if j == -1:
            result = 1
            break
        elif txt[idx] in wrd_dict:
            idx += wrd_dict[txt[idx]]
        else:
            idx += N

    print(f'#{tc+1} {result}')