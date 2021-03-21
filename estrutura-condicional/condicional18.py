"""
Faça um programa que mostre ao usuário um menu com 4 opções de
operações matemáticas (as básicas, por exemplo). O usuário escolhe
uma das opções e o seu programa então pede dois valores numéricos
e realiza a operação, mostrando o resultado e saindo.
"""

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

escolha = int(input("Digite 1 para somar, 2 para subtrair, 3 para multiplicar e 4 para dividir: "))

if escolha == 1:
    print(f"Soma: {numero1 + numero2}")
elif escolha == 2:
    print(f"Subtração: {numero1 - numero2}")
elif escolha == 3:
    print(f"Multiplicação: {numero1 * numero2}")
elif escolha == 4:
    print(f"Divisão: {numero1 / numero2}")
else:
    print("Escolha inválida")
