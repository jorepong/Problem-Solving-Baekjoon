n, m = map(int, input().split())

pokedex_by_num = [None]*(n+1)
pokedex_by_name = {}

for i in range(n):
    pokemon = input()
    pokedex_by_num[i+1] = pokemon
    pokedex_by_name[pokemon] = i+1

for _ in range(m):
    s = input()

    if s.isdigit():
        print(pokedex_by_num[int(s)])
    else:
        print(pokedex_by_name[s])