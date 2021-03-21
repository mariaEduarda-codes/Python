"""
Faça um programa que receba dois números e mostre o maior.
Se por acaso, os dois números forem iguais, imprima a
mensagem Números iguais.
"""

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

if numero1 > numero2:
    print(f"Maior: {numero1}")
elif numero2 == numero1:
    print(f"São iguais! ")
else:
    print(f"Maior: {numero2}")
