N = int(input())


def bottom_up_fibonacci(n):
    dp_table = [-1] * (n+1)
    dp_table[0] = 0
    dp_table[1] = 1
    for i in range(2, n + 1):
        dp_table[i] = dp_table[i-1] + dp_table[i-2]
    return dp_table


def recur(n):
    if n <= 1:return n
    return recur(n-2)+recur(n-1)
print(recur(N))