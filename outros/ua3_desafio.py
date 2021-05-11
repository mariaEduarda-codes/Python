"""
Desenvolva um programa que recebe um caractere digitado pelo teclado utilizando
a função input e retorne, utilizando a função print, esse caractere convertido
em decimal, hexadecimal e binário, conforme exemplo abaixo:

Digite uma letra: Z
Letra digitada foi: Z
Seu valor em decimal é: 90
Seu valor em hexadecimal é: 0x5a
Seu valor em binário é: 0b1011010
"""

caractere = str(input('Digite uma letra: '))
print(f'Letra digitada foi: {caractere}')
decimal = ord(caractere)
hexadecimal = hex(decimal)
binario = bin(decimal)
print(f'Seu valor em decimal é: {decimal}')
print(f'Seu valor em hexadecimal é: {hexadecimal}')
print(f'Seu valor em binário é: {binario}')
