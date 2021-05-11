"""
Faça uma função que receba a distância em Km e a quantidade de litros
de gasolina consumidos por um carro em um percurso, calcule o consumo
em Km/l e escreva uma mensagem de acordo com a tabela abaixo:

CONSUMO         Km/l        MENSAGEM
menor que       8           Venda o carro!
entre           8 e 12      Carro econômico!
maior que       12          Carro super econômico!
"""


def calc_consumo(distancia, gasolina):
    consumo = distancia / gasolina
    return consumo


def mostra_mensagem(consumo):
    if consumo < 8:
        print('Venda o carro')
    elif 8 < consumo < 12:
        print('Carro econômico')
    else:
        print('Carro super econômico')


dist_percorrida = float(input("Digite a distância em km: "))
litros_gasolina = float(input("Digite a qtd. de gasolina em litros: "))

mostra_mensagem(calc_consumo(dist_percorrida, litros_gasolina))
