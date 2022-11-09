def solution(line):
    answer = []
    n = len(line)

    i = 0
    stack = ''
    flag = False
    while i < n:

        # 이전 문자가 있을때
        if stack:

            # 이전 문자가 있다면 *표 표기 True
            if stack[-1] == line[i]:
                flag =True

            # 다르다면
            else:
                # *표 표기 True면 *표도 같으 append
                answer.append(stack)
                if flag:
                    answer.append('*')
                    flag = False
                stack = line[i]

        # 이전 문자가 없다면 이전 문자 갱신
        else:
            stack = line[i]

        i += 1

    if stack:
        answer.append(stack)
        if flag:
            answer.append('*')

    return answer

print(solution('aabbbc'))
print(solution('hellllllo'))
print(solution('wonderful'))