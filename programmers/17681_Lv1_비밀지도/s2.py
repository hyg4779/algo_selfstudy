def solution(n, arr1, arr2):
    ans = []
    for i, j in zip(arr1, arr2):
        mat = bin(i|j)[2:].rjust(n, '0').replace('1', '#').replace('0', ' ')
        ans.append(mat)
    print(ans)

    return ans

solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])