"""
Escreva um programa que, dados dois números inteiros, mostre
na tela o maior deles, assim como a diferença existente entre
ambos.
"""

numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))

if numero1 > numero2:
    print(f"Maior: {numero1}")
    print(f"Diferença entre ambos: {numero1 - numero2}")
else:
    print(f"Maior: {numero2}")
    print(f"Diferença entre ambos: {numero2 - numero1}")
