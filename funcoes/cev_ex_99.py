"""
Faça um programa que tenha uma função chamada maior(), que
recebe vários parâmetros com valores inteiros. Seu programa
tem que analisar todos os valores e dizer qual deles é o maior.
"""


def maior(*args):
    maior_valor = 0
    contagem = 0
    for valor in args:
        if valor > maior_valor:
            maior_valor = valor
        contagem += 1
    print(f'Foram recebidos {contagem} valores e o maior é {maior_valor}')


maior(2, 5, 9, 7, 12, 20, 16, 4)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
