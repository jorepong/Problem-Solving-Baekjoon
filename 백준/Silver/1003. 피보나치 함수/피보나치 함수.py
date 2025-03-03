import sys

dp = {
    0: (1, 0),
    1: (0, 1)
}

n = int(sys.stdin.readline().strip())

def fib(i):
    if i not in dp:
        t1 = fib(i-1)
        t2 = fib(i-2)
        dp[i] = (t1[0] + t2[0], t1[1] + t2[1])

    return dp[i]

for _ in range(n):
    i = int(sys.stdin.readline().strip())
    output = fib(i)
    print(output[0], output[1])