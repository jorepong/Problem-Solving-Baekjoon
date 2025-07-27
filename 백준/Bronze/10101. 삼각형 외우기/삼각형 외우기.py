import sys

angles = []
for _ in range(3):
    angles.append(int(sys.stdin.readline().strip()))

def solve(a, b, c):
    if (a + b + c) != 180:
        return "Error"

    if a == 60 and b == 60 and c == 60:
        return "Equilateral"

    if (a == b and b != c) or (b == c and c != a) or (a == c and a != b):
        return "Isosceles"

    return "Scalene"

print(solve(angles[0], angles[1], angles[2]))