'''
LIFO
top: -1 , 하나씩 추가될 때마다 +1 / 빠질 때마다 -1
python에서 stack을 list로 씀
장점: 구현이 용이
리스트의 크기를 변경하기 위해는 내부적으로 overhead 발생

'''

def fibo(n):
    """
    memoization:DP의 핵심이 되는 기술
    피보나치 수열

    # memo를 위한 리스트를 생성하고 memo[0]을 0, memo[1]을 1로 저장
    """
    global memo

    if n >=2 and len(memo) <= 2:
        memo.append(fibo(n-1)+fibo(n-2))
    return memo[n]

memo = [0, 1]

"""
DP: 최적화 문제를 해결하는 알고리즘
1. recursive
2. iterative
점화식을 찾는 것이 관건
"""

def dp_fibo(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])

    return f[n]