"""
Faça uma função que receba dois números inteiros positivos por parâmetro
e retorne a soma dos N números inteiros existentes entre eles.
"""


def somar_inteiros(inicio, final):
    soma = 0
    index = 0
    lista = []
    for numero in range(inicio+1, final):
        soma += numero
        lista.append(numero)
        lista[index] = numero
        index += 1
    print(f'Os números entre {inicio} e {final} são: {lista}.')
    print(f'A soma deles é {soma}')


num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
somar_inteiros(num1, num2)
