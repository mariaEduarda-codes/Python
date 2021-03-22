"""
Fazer um programa para ler os três coeficientes de uma
equação do segundo grau. Usando a fórmula de Bhaskara,
calcular e mostrar os valores das raízes x1 e x2 da equação
com quatro casas decimais, conforme exemplo. Se a equação
não possuir raizes reais, mostrar uma mensagem.
"""
import math

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

delta = b ** 2 - (4 * a * c)

if a == 0:
    print("A equação não é do 2º grau, pois a é igual a 0")
else:
    if delta < 0:
        print("A equação não possui raizes reais")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
