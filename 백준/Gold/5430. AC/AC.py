from collections import deque

t = int(input())

for _ in range(t):
    functions = input()
    n = int(input())
    if n != 0:
        arr = list(map(int, input()[1:-1].split(',')))
    else:
        input()
        arr = []

    queue = deque(arr)
    front = True

    error = False
    for f in list(functions):
        if f == 'R':
            front = not front
        else:
            if len(queue) == 0:
                print("error")
                error = True
                break

            if front:
                queue.popleft()
            else:
                queue.pop()

    if not error:
        if not front:
            print(f"[{','.join(map(str, list(reversed(queue))))}]")
        else:
            print(f"[{','.join(map(str, list(queue)))}]")