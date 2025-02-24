import sys

num = int(sys.stdin.readline())

def draw_blank(n):
    output = []
    for _ in range(n):
        output.append(' '*n)
    return output

def draw_star(n):
    if n == 3:
        return ["***", "* *", "***"]

    outputs = [''] * n
    for i in range(9):
        if i == 4:
            ret = draw_blank(n//3)
        else:
            ret = draw_star(n//3)

        for k in range(n//3):
            if i in [3, 4, 5]:
                outputs[k+(n//3)] += ret[k]
            elif i in [6, 7, 8]:
                outputs[k+(n//3)*2] += ret[k]
            else:
                outputs[k] += ret[k]

    return outputs

ret = draw_star(num)
for line in ret:
    print(line)