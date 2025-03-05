import sys

M = int(sys.stdin.readline().strip())

pocket = set()
for _ in range(M):
    line = sys.stdin.readline().strip().split()
    command = line[0]

    if command == "all" or command == "empty":
        if command == "all":
            pocket = set(range(1, 21))
        else:
            pocket.clear()
    else:
        value = int(line[1])
        if command == "add":
            pocket.add(value)
        elif command == "remove":
            if value in pocket:
                pocket.remove(value)
        elif command == "check":
            if value in pocket:
                print(1)
            else:
                print(0)
        elif command == "toggle":
            if value in pocket:
                pocket.remove(value)
            else:
                pocket.add(value)