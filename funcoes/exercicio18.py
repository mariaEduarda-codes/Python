"""
Faça uma função que recebe por parâmetro dois valores inteiros X e Z.
Calcule e retorne o resultado de x elevado a z para o programa principal.
"""


def expoente(x, z):
    return x ** z


num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
print(expoente(num1, num2))
