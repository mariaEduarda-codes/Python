"""
Faça um programa que tenha uma função chamada contador(), que recebe
três parâmetros: inicio, fim e passo. Seu programa tem que realizar
três contagens através da função criada:

a) De 1 até 10, de 1 em 1;
b) De 10 até 0, de 2 em 2;
c) Uma contagem personalizada.
"""


def contador(inicio, fim, passo=1):
    if passo == 0:
        passo = 1
    if inicio < fim and passo > 0:
        for valor in range(inicio, fim+1, passo):
            print(valor, end=' ')
    elif inicio < fim and passo < 0:
        for valor in range(inicio, fim+1, - passo):
            print(valor, end=' ')
    elif inicio > fim and passo > 0:
        for valor in range(inicio, fim-1, - passo):
            print(valor, end=' ')
    elif inicio > fim and passo < 0:
        for valor in range(inicio, fim-1, passo):
            print(valor, end=' ')
    print()


print('Contando de 1 até 10, de 1 em 1: ')
contador(1, 10)
print('Contando de 10 até 0, de 2 em 2: ')
contador(10, 0, 2)
print('Agora, personalize sua contagem: ')

valor_inicio = int(input("Valor de início: "))
valor_fim = int(input("Valor final: "))
valor_de_passo = int(input("Valor de passo: "))

contador(valor_inicio, valor_fim, valor_de_passo)
