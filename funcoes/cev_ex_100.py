"""
Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e soma_par(). A primeira função vai sortear 5 números
e vai coloca-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores pares sorteados pela função anterior.
"""
from random import randint


def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(n, end=' ')


def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista}, sua soma é {soma}')


numeros = list()
sorteia(numeros)
soma_par(numeros)
