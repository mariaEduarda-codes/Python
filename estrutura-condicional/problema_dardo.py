"""
No arremesso de dardo, o atleta tem três chances para
lançar o dardo à maior distância que conseguir. Você
deve criar um programa para, dadas as medidas das três
tentativas de lançamento, informar qual foi a maior.
"""

print("Digite as três distâncias: ")
d1 = float(input())
d2 = float(input())
d3 = float(input())

if d1 > d2 and d1 > d3:
    maior = d1
elif d2 > d1 and d2 > d3:
    maior = d2
else:
    maior = d3

print(f"MAIOR DISTÂNCIA = {maior:.2f}")
