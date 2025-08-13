import sys


def is_hansu(num):
    digits = list(map(int, str(num)))

    if len(digits) >= 3:
        diff = digits[1] - digits[0]
        for i in range(1, len(digits) - 1):
            if digits[i + 1] - digits[i] != diff:
                return False
            
    return True


try:
    N = int(sys.stdin.readline())
except ValueError:
    N = 0

if N < 100:
    print(N)
else:
    count = 99
    for i in range(100, N + 1):
        if is_hansu(i):
            count += 1

    print(count)