import sys


def gcd(n, m):
    if m > n:
        n, m = m, n

    if n % m == 0:
        return m

    return gcd(m, n % m)

def lcm(n, m):
    return int(n * m / gcd(n, m))

n, m = map(int, sys.stdin.readline().strip().split())

print(gcd(n, m))
print(lcm(n, m))