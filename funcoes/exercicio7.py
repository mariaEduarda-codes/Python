"""
Faça uma função que recebe uma temperatura em graus Celsius e retorne-a
convertida em graus Fahrenheit. A fórmula de conversão é: F = C * (9.0/5.0) + 32.0,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""


def converte_temperatura(celsius):
    fahrenheit = celsius * (9.0/5.0) + 32.0
    return fahrenheit


temp_celsius = float(input("Digite a temperatura em Celsius: "))
temp_fahrenheit = converte_temperatura(temp_celsius)
print(f'{temp_celsius}º C equivale a {temp_fahrenheit}ºF')
