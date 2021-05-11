"""
Crie um programa que recebe três valores (obrigatoriamente maiores que zero),
representando as medidas dos três lados de um triângulo. Elabore funções para:

(a) Determinar se os lados formam um triângulo, sabendo que:
    O comprimento de cada lado de um triângulo é menor do que a soma dos
        outros dois lados.
(b) Determinar e mostrar o tipo de triângulo, caso as medidas formem um
triângulo. Sendo que:
    Chama-se equilátero o triângulo que tem três lados iguais.
    Denomina-se isósceles o triângulo que tem o comprimento de dois lados
        iguais.
    Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""


def verifica_triangulo(lado_a, lado_b, lado_c):  # Checa se as medidas informadas formam um triângulo
    if lado_a < (lado_b + lado_c):
        triangulo = True
    elif lado_b < (lado_a + lado_c):
        triangulo = True
    elif lado_c < (lado_a + lado_b):
        triangulo = True
    else:
        triangulo = False

    if triangulo:
        print('É um triângulo.')
        return True
    else:
        print('Não satisfaz a condição de triângulo.')
        return False


def verifica_tipo_triangulo(lado_a, lado_b, lado_c):  # Checa qual o tipo de triângulo informado
    if lado_a == lado_b == lado_c:
        return 'Equilátero'
    elif lado_a == lado_b:
        return 'Isósceles'
    elif lado_a == lado_c:
        return 'Isósceles'
    elif lado_b == lado_c:
        return 'Isósceles'
    else:
        return 'Escaleno'


print('-- VERIFICANDO TRIÂNGULOS --')
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

if verifica_triangulo(a, b, c) is True:
    print(verifica_tipo_triangulo(a, b, c))
