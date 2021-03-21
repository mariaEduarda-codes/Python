import math

"""
Leia um número fornecido pelo usuário. Se esse número
for positivo, calcule a raiz quadrada do número. Se o
número for negativo, mostre uma mensagem dizendo que o
número é inválido
"""
numero1 = int(input("Digite um número: "))

if numero1 > 0:
    print(math.sqrt(numero1))
else:
    print("Número inválido")
