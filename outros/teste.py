valores = [7, 2, 5, 0, 4]
print(valores)


def dobra_valores(lst):
    posicao = 0
    while posicao < len(lst):
        lst[posicao] *= 2
        posicao += 1

    print(lst)


dobra_valores(valores)
dobra_valores([8, 10, 12, 20])
