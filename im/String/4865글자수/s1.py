import sys
sys.stdin = open('sample_input.txt')



for tc in range(int(input())):
    txt1 = input()
    txt2 = input()

    word_dict = {arg: 0 for arg in txt1}

    for t in txt2:
        if t in word_dict:
            word_dict[t] += 1


    print(f'#{tc+1} {max(word_dict.values())}')

