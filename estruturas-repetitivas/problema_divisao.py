"""
Escreva um algoritmo que leia dois números e imprima
o resultado da divisão do primeiro pelo segundo. Caso
não for possível, mostre a mensagem "DIVISÃO IMPOSSÍVEL".
"""

n = int(input("Quantos casos você vai digitar? "))

for i in range(0, n):
    numerador = float(input("Entre com o numerador: "))
    denominador = float(input("Entre com o denominador: "))
    if denominador == 0:
        print("DIVISÃO IMPOSSÍVEL")
    else:
        print(f"DIVISÃO = {numerador/denominador}")
