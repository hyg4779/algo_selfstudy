def solution(text):
    arr = ['a', 'e', 'i', 'o', 'u']
    answer = 0
    for i in text:
        if i in arr:answer += 1
    return answer