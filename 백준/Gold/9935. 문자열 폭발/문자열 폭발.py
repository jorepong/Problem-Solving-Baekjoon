import sys

line = sys.stdin.readline().strip()
explosion_str = sys.stdin.readline().strip()
explosion_str_len = len(explosion_str)

stack = []
for c in line:
    stack.append(c)
    stack_len = len(stack)
    if stack_len >= explosion_str_len and ''.join(stack[stack_len - explosion_str_len:]) == explosion_str:
        for _ in range(explosion_str_len):
            stack.pop()

print(''.join(stack) if len(stack) > 0 else 'FRULA')