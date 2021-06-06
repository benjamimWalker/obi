a_l = [int(x) for x in input().split()] # fotografia obi 2020 segunda fase sênior: nove linhas bro
numero_de_molduras = int(input())
molduras = [[] * x for x in range(numero_de_molduras)]
for c in range(numero_de_molduras):
    molduras[c] = [int(x) for x in input().split()]
molduras_inity = molduras.copy()
molduras = list(filter(lambda moldura: (a_l[0] <= moldura[0] and a_l[1] <= moldura[1]) or (a_l[0] <= moldura[1] and a_l[1] <= moldura[0]), list(filter(lambda moldura: moldura[0] * moldura[1] >= a_l[0] * a_l[1], molduras))))
moldura_t = list(map(lambda moldura: moldura[0] * moldura[1], molduras))
print(-1 if not molduras else molduras_inity.index(molduras[moldura_t.index(min(moldura_t))]) + 1)
