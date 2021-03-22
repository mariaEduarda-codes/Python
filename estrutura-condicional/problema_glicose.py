"""
Fazer um programa para ler a quantidade de glicose
no sangue de uma pessoa e depois mostrar na tela a
classificação desta glicose de acordo com a tabela
de referência abaixo.

CLASSIFICAÇÃO       GLICOSE
Normal              Até 100mg/dl
Elevado             Maior que 100 até 140 mg/dl
Diabetes            Maior que 140 mg/dl
"""

glicose = float(input("Digite a medida da glicose: "))

if glicose <= 100:
    print("Classificação: Normal")
elif (glicose > 100) and glicose <= 140:
    print("Classificação: Elevado")
else:
    print("Classificação: diabetes")
