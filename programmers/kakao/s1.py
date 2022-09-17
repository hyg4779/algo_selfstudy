from collections import deque
number_dict = {'qw': '1', 'as': '2', 'zx': '3', 'we': '4', 'sd': '5', 'xc': '6', 'er': '7', 'df': '8', 'cv': '9', 'ze': '0'}

n = int(input())
number = input()

tmp = number_dict[number[:2]]
Q = deque([(tmp, 2, False)])
results = list()

while Q:
    now, idx, check = Q.popleft()

    if idx >= n:
        results.append(now)
        continue

    if not check and number[idx-1:idx+1] in number_dict:
        Q.append((now+number_dict[number[idx-1:idx+1]], idx, True))

    if idx+1 <= n:
        Q.append((now+number_dict[number[idx:idx+2]], idx+2, False))


print(results[-1])