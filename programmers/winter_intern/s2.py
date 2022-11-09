arr = [[0]*5120 for _ in range(1800)]


field = []
for i in range(0, 1800, 4):
    # mat = 4*1800 list
    mat = arr[i:i+4]

    temp = []
    for j in range(0, 5120, 256):
        tmp = []
        for k in range(4):
            # print(len(mat))
            # print(len(mat[0]))
            # print(i, k, j)
            tmp.append(mat[k][j:j+256])

        # tmp = 4*256 list
        temp.append(tmp)

    field.append(temp)

print(len(field))
print(len(field[0]))
print(len(field[0][0]))
print(len(field[0][0][0]))