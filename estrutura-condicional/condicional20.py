"""
Dados três valores, A, B e C, verificar se eles podem ser valores
dos lados de um triângulo e, se forem, se é um triângulo escaleno,
equilátero ou isósceles, considerando os seguintes conceitos:

O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados
Chama-se equilátero o triângulo que tem três lados iguais
Denomina-se isósceles o triângulo que tem o comprimento de dois lados iguais
Recebe o nome de escaleno o triângulo que tem os três lados diferentes
"""

a = float(input("Insira o valor do lado A: "))
b = float(input("Insira o valor do lado B: "))
c = float(input("Insira o valor do lado C: "))

if a == b == c:
    print("Triângulo equilátero")
elif (a == b) or (b == c) or (a == c):
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")
