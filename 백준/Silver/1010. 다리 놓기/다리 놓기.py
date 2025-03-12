import sys

T = int(sys.stdin.readline().strip())

fact = [1] * 31

for i in range(1, 31):
    fact[i] = fact[i-1] * i

for _ in range(T):
    n, m = map(int, sys.stdin.readline().strip().split())
    print(int(fact[m] / (fact[m-n] * fact[n])))