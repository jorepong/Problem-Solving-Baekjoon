def solution(k, d):
    answer = 0

    x = (d // k) * k
    y = 0

    while x ** 2 + y ** 2 <= d ** 2:
        answer += (x // k) + 1
        y += k

        while x >= 0 and y >= 0 and x ** 2 + y ** 2 > d ** 2:
            x -= k

    return answer