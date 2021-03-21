"""
Faça um programa que receba a altura e o sexo de uma pessoa
e calcule e mostre seu peso ideal, utilizando as seguintes
fórmulas (onde h corresponde à altura):
Homens: (72.7 * h) - 58
Mulheres: (62.1 * h) - 44.7
"""

sexo = input("Digite seu sexo: (H) para homem e (M) para mulher ")
altura = float(input("Digite sua altura: "))

if sexo == "h" or "H":
    print(f"Seu peso ideal é: {(72.7 * altura) - 58}")
elif sexo == "m" or "M":
    print(f"Seu peso ideal é: {(62.1 * altura) - 44.7}")
