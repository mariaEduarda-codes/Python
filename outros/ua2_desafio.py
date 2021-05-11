"""
Você se propõe a desenvolver um programa com as seguintes características:

Três variáveis globais do tipo float, inicializadas com um valor padrão qualquer.
Implementação de três funções:

ler_numeros(), que faz a leitura das três variáveis
globais do tipo float e imprime os números na tela com a função 'f';

calcular_soma(), que calcula a soma dos três números lidos por meio de uma variável local
e imprime essa variável na tela com a instrução 'f'.

calcular_media(), que calcula a média dos três números lidos com o auxílio de uma variável
local e imprime a média na tela com a instrução 'f'.
"""

num1 = 1
num2 = 1
num3 = 1


def ler_numeros():
    global num1
    global num2
    global num3
    num1 = float(input('Digite o 1º número: '))
    num2 = float(input('Digite o 2º número: '))
    num3 = float(input('Digite o 3º número: '))
    print(f'Os números lidos são: {num1}, {num2} e {num3}')


def calcular_soma(a, b, c):
    soma = a + b + c
    print(f'A soma é: {soma:.1f}')


def calcular_media(a, b, c):
    media = (a + b + c)/3
    print(f'A média é: {media:.1f}')


ler_numeros()
calcular_soma(num1, num2, num3)
calcular_media(num1, num2, num3)
