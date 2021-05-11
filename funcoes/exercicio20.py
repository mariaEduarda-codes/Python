"""
Faça um algoritmo que receba um número inteiro
positivo n e calcule o seu fatorial n!
"""


def calcula_fatorial(n):
    fatorial = n
    for num in range(n-1, 0, -1):
        fatorial *= num
    print(fatorial)


numero = int(input('Digite um número inteiro positivo: '))
calcula_fatorial(numero)
