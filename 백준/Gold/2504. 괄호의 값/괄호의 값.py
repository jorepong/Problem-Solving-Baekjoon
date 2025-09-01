import sys

bracket_srt = sys.stdin.readline()

temp = 1
answer = 0
stack = []

for i in range(len(bracket_srt)):
    if bracket_srt[i] == '(':
        stack.append('(')
        temp *= 2
    elif bracket_srt[i] == '[':
        stack.append('[')
        temp *= 3
    elif bracket_srt[i] == ')':
        if not (stack and stack[-1] == '('):
            answer = 0
            break

        if bracket_srt[i-1] == '(':
            answer += temp

        temp = temp // 2
        stack.pop()
    elif bracket_srt[i] == ']':
        if not (stack and stack[-1] == '['):
            answer = 0
            break

        if bracket_srt[i-1] == '[':
            answer += temp

        temp = temp // 3
        stack.pop()

print(0 if stack else answer)