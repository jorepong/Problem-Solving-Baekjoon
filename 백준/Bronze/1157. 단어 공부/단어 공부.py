import sys

word = sys.stdin.readline().strip()

alphas = [0] * 26

most_used = None
count = 0
multiple = False

for char in word:
    i = ord(char.lower()) - ord('a')
    alphas[i] += 1
    if alphas[i] == count:
        multiple = True
    elif alphas[i] > count:
        most_used = char.upper()
        count = alphas[i]
        multiple = False

if multiple:
    print('?')
else:
    print(most_used)