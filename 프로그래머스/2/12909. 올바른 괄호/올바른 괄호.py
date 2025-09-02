def solution(s):
    answer = True
    
    stack = []
    
    for c in s:
        if c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        else:
            stack.append('(')

    return True if len(stack) == 0 else False