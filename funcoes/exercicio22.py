"""
Crie uma função que receba como parâmetro um valor inteiro e gere
como saída n linhas com ponto de exclamação, conforme o exemplo
abaixo (para n = 5):

!
!!
!!!
!!!!
!!!!!
"""


def imprime_excalamacao(inteiro):
    for numero in range(1, inteiro+1):
        print('!' * numero)


n = int(input('Digite um número inteiro: '))
imprime_excalamacao(n)
