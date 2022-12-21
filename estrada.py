import sys
sys.setrecursionlimit(110000) # estrada obi 2020 segunda fase sênior


def calc(index: int, actualpoint: float):
    if index == len(cidades) - 1:
        values.append(t - actualpoint)
        return None
    elif index == 0:
        temp = (cidades[index] + cidades[index + 1]) / 2
        values.append(temp)
        calc(index + 1, temp)
    else:
        temp = (cidades[index] + cidades[index + 1]) / 2
        temp2 = (temp - cidades[index]) + (cidades[index] - actualpoint)
        values.append(temp2)
        calc(index + 1, temp)


cidades, values, t = [], [], int(input())

for c in range(int(input())):
    cidades.append(int(input()))

cidades.sort()
calc(0, 0)
print(f'{min(values):.2f}')  #
