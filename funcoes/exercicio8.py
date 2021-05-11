"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela
equação: hipotenusa = math.sqrt(a² + b²). Faça uma função que receba os
valores de a e b e calcule o valor da hipotenusa através da equação.
"""
import math


def calc_hipotenusa(cat_a, cat_b):
    hipotenusa = math.sqrt(cat_a ** 2 + cat_b ** 2)
    return f'{hipotenusa:.2f}'


a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))
print(f'O valor da hipotenusa é: {calc_hipotenusa(a, b)}')
