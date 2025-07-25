import sys

l, c = map(int, sys.stdin.readline().strip().split())

vowels = {'a', 'e', 'i', 'o', 'u'}
chars = sys.stdin.readline().strip().split(' ')
chars.sort()

def dfs(index, path, cn, vn):
    if cn > l - len(path) or vn > l - len(path):
        return

    if len(path) == l:
        print(''.join(path))
        return

    for i in range(index, c):
        if chars[i] in vowels:
            dfs(i + 1, path + [chars[i]], cn, vn - 1)
        else:
            dfs(i + 1, path + [chars[i]], cn - 1, vn)

dfs(0, [], 2, 1)