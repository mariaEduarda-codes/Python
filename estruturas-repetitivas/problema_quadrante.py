"""
Escreva um programa para ler as coordenadas (X, Y) de
uma quantidade indeterminada de pontos no sistema
cartesiano. Para cada ponto escrever o quadrante a que
ele pertence (Q1, Q2, Q3 ou Q4). O algoritmo será encerrado
quando pelo menos uma de duas coordenadas for NULA (nesta
situação sem escrever mensagem alguma).
"""
print("Digite os valores das coordenadas X e Y: ")
x = float(input())
y = float(input())

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("QUADRANTE Q1")
    elif (x < 0) and y > 0:
        print("QUADRANTE Q2")
    elif (x < 0) and y < 0:
        print("QUADRANTE Q3")
    elif (x > 0) and y < 0:
        print("QUADRANTE Q4")
    print("Digite os valores das coordenadas X e Y: ")
    x = float(input())
    y = float(input())
