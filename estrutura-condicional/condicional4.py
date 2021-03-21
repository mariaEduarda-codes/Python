import math
"""
Faça um programa que leia um número e, caso ele seja positivo, calcule
e mostre:
(a) O número digitado ao quadrado
(b) A raiz quadrada do número digitado
"""

numero = float(input("Digite um número: "))

if numero > 0:
    print(pow(numero, 2))
    print(math.sqrt(numero))
else:
    print("Não foi possível completar a ação."
          " Número não é positivo.")
