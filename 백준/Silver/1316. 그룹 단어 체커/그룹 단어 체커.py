import sys

n = int(sys.stdin.readline().strip())
count = 0

for _ in range(n):
    word = sys.stdin.readline().strip()

    checked = set()
    last = word[0]
    is_group_word = True

    for i in range(1, len(word)):
        if word[i] in checked:
            is_group_word = False
            break
        if word[i] != last:
            checked.add(word[i-1])
            last = word[i]

    if is_group_word:
        count += 1

print(count)