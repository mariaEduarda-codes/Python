import math
"""
Leia um número real. Se o número for positivo imprima a 
raiz quadrada. Do contrário, imprima o número ao quadrado.
"""

numero = float(input("Digite um número real: "))

if numero > 0:
    print(math.sqrt(numero))
else:
    print(pow(numero, 2))
