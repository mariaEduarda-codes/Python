"""
Faça uma função e um programa de teste para o cálculo do volume de uma esfera.
Sendo que o raio é passado por parâmetro.
V = 4/3 * pi * r³
"""
import math


def calc_volume(raio):
    volume = 4/3 * math.pi * (raio ** 3)
    return f'{volume:.2f}'


valor_raio = float(input("Digite o valor do raio: "))
print(calc_volume(valor_raio))
