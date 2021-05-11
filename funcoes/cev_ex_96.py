"""
Faça um programa que tenha uma função chamada área(), que recebe as
dimensões de um terreno retangular (largura e comprimento) e mostre
a área do terreno.
"""


def area(largura, compr):
    print(f'A área de um terreno retangular {largura} X {compr} é {largura * compr}m²')


larg = float(input("Digite a largura: "))
comprimento = float(input("Digite o comprimento: "))
area(larg, comprimento)
