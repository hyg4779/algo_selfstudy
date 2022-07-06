def binary(n, mat):
    res = []
    for i in range(n):
        num = mat[i]

        tmp = ''
        if num:
            while num > 1:
                tmp = '1' + tmp if num%2 else '0' + tmp
                num //= 2
            tmp = '1' + tmp

        else:
            tmp = '0'
        if len(tmp) < n:tmp = '0'*(n-len(tmp)) + tmp
        res.append(tmp)

    return res

def solution(n, arr1, arr2):

    mat1, mat2 = binary(n, arr1), binary(n, arr2)
    ans = ['' for _ in range(n)]
    print(mat1)
    print(mat2)
    for i in range(n):
        for j in range(n):
            ans[i] += '#' if mat1[i][j] == '1' or mat2[i][j] == '1' else ' '

    return ans

# print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))