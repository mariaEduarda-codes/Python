"""
Leia um valor inteiro N. Este valor será a quantidade de
números inteiros que serão lidos em seguida. Para cada
valor lido, mostre uma mensagem dizendo se este valor
lido é PAR ou ÍMPAR, e também se é POSITIVO ou NEGATIVO.
No caso do valor ser igual a zero (0), seu programa
deverá imprimir apenas NULO.
"""

n = int(input("Quantos números você vai digitar? "))

for i in range(0, n):
    x = int(input("Digite um número: "))
    if (x > 0) and (x % 2 == 0):
        print("PAR POSITIVO")
    elif (x > 0) and (x % 2 != 0):
        print("ÍMPAR POSITIVO")
    elif (x < 0) and (x % 2 == 0):
        print("PAR NEGATIVO")
    elif (x < 0) and (x % 2 != 0):
        print("ÍMPAR NEGATIVO")
    elif x == 0:
        print("NULO")
