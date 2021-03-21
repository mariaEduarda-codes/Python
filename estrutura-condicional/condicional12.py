"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem 
"Número inválido". Se o número for positivo, calcular o logaritmo desse número.
"""
import math

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print(f"{math.log(numero)}")
else:
    print("Número inválido")
