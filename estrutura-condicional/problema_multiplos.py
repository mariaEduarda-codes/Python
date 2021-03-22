"""
Fazer um programa para ler dois números inteiros, e dizer
se um número é múltiplo do outro. Os números podem ser
digitados em qualquer ordem.
"""

print("Digite dois números inteiros: ")
n1 = int(input())
n2 = int(input())

if n1 % n2 == 0 or n2 % n1 == 0:
    print("São múltiplos")
else:
    print("Não são múltiplos")
