"""
Faça um algoritmo que calcule o IMC de
uma pessoa e mostre sua classificação
de acordo com a tabela abaixo:

IMC             CLASSIFICAÇÃO
< 18,5          Abaixo do peso
18,6 - 24,9     Saudável
25,0 - 29,9     Peso em excesso
30,0 - 34,9     Obesidade Grau I
35,0 - 39,9     Obesidade Grau II (severa)
>= 40,0         Obesidade Grau III (mórbida)
"""

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)
print(imc)

if imc < 18.5:
    print("Abaixo do peso")
elif (imc >= 18.6) and (imc <= 24.9):
    print("Saudável")
elif (imc >= 25) and (imc <= 29.9):
    print("Peso em excesso")
elif (imc >= 30) and (imc <= 34.9):
    print("Obesidade Grau I")
elif (imc >= 35) and (imc <= 39.9):
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")
