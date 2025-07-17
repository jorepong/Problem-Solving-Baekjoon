import sys

n = int(sys.stdin.readline())

if n == 1:
    print(0)
    exit()

is_prime = [True] * (n + 1)
is_prime[0], is_prime[1] = False, False

for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

primes = [i for i, prime in enumerate(is_prime) if prime]
num_primes = len(primes)

count = 0
current_sum = 0
start = 0
end = 0

while end <= num_primes:
    if current_sum >= n:
        if current_sum == n:
            count += 1
        current_sum -= primes[start]
        start += 1
    elif end == num_primes:
        break
    else:
        current_sum += primes[end]
        end += 1

print(count)