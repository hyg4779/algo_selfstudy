def Brute_force(text, word):
    i = 0
    j = 0

    M = len(word)   # 찾는 단어의 길이
    N = len(text)   # 탐색되는 문장의 길이

    while j < M and i < N:
        if word[j] != text[i]:
            i = i - j
            j = -1

        i += 1
        j += 1
    return 1 if j == M else 0

'''
Brute-force: 고지식한 알고리즘
찾는 문자 열이 제일 마지막에 있을 때
시간복잡도가 M*N으로 늘어남
'''