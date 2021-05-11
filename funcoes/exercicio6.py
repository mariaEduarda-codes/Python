"""
Faça uma função que receba 3 números inteiros como parâmetro, representando
horas, minutos e segundos, e os converta em segundos.
"""


def converte_em_segundos(horas, minutos, segundos):

    return horas * 3600 + minutos * 60 + segundos


h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))
resultado = converte_em_segundos(h, m, s)
print(resultado)
