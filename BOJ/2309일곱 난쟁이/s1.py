res, cnt = 0, 0
array = [int(input())for _ in range(9)]


def search(v, s, people, cnt):
    if v > 100:return False

    if cnt == 7 and v == 100:
        people.sort()
        for p in people:
            print(p, end='\n')
        exit()

    for idx in range(s, 9):
        search(v+array[idx], s+1, people+[array[idx]], cnt+1)


for i in range(3):
    arr = [array[i]]
    search(array[i], i+1, arr, 1)
