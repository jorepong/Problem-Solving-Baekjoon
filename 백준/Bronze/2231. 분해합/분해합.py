n = int(input())

def solve(num):
    for i in range(num+1):
        divided_sum = i

        for c in list(str(i)):
            divided_sum += int(c)
            
        if divided_sum == num:
            return i
    return 0

print(solve(n))