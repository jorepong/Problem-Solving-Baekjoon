import sys
sys.setrecursionlimit(10**6)

N, r, c = map(int, sys.stdin.readline().strip().split())

base = [
    [0, 1],
    [2, 3]
]

def solve(n, x, y):
    if n == 1:
        return base[x][y]

    if 0 <= x < 2**(n-1) and 0 <= y < 2**(n-1): #2사분면
        return solve(n-1, x, y)
    elif 0 <= x < 2**(n-1) and 2**(n-1) <= y: #1사분면
        return (2**(n-1))**2 + solve(n-1, x, y - 2**(n-1))
    elif 2**(n-1) <= x and 0 <= y < 2**(n-1): #3사분면
        return ((2**(n-1))**2)*2 + solve(n-1, x - 2**(n-1), y)
    else: #4사분면
        return ((2**(n-1))**2)*3 + solve(n-1, x - 2**(n-1), y - 2**(n-1))

print(solve(N, r, c))