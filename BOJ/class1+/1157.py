word = input().rstrip()  # 입력 단어를 받고 오른쪽 공백 제거

alpha_list = [0] * 26  # 알파벳 등장 횟수를 저장할 리스트 초기화

for char in word:
    if char.isalpha():
        index = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
        alpha_list[index] += 1  # 알파벳 등장 횟수 증가

max_count = max(alpha_list)  # 가장 많이 등장한 알파벳의 횟수

if alpha_list.count(max_count) > 1:
    print("?")  # 동일한 등장 횟수를 가진 알파벳이 여러 개 존재하는 경우
else:
    max_index = alpha_list.index(max_count)  # 가장 많이 등장한 알파벳의 인덱스
    print(chr(max_index + ord('A')))  # 가장 많이 등장한 알파벳 출력
