"""
Fazer um programa que lê números inteiros
até que um 0 seja lido. Depois mostrar a
soma dos números lidos.
"""

numero = int(input("Digite um número: "))
soma = numero

while numero != 0:
    numero = int(input("Digite outro número: "))
    soma += numero

print(f"SOMA = {soma}")
