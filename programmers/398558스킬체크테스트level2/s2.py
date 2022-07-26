def solution(numbers):

    result = []
    for num in numbers:
        answer = float('inf')
        b_num = ['0'] + list(bin(num)[2:])

        idx = 1

        while True:

            tmp = bin(num+idx)[2:]

            cnt = 0
            for i in range(len(tmp)-1, -1, -1):
                if tmp[i] != b_num[i]:
                    cnt += 1
                if cnt == 3:
                    break

            else:
                val = 0
                for i in range(len(tmp)):
                    val += int(tmp[i])*2**(len(tmp)-1-i)
                if val > num:
                    result.append(val)
                    break
            idx += 1
    return result

print(solution([2, 7]))