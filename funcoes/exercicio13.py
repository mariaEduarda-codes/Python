"""
Faça uma função que receba dois valores numéricos e um símbolo. Este símbolo
representar-a a operação que se deseja efetuar com os números. Se o símbolo
for + deverá ser realizada uma adição, se for - uma subtração, se for / uma
divisão e se for * será efetuada uma multiplicação.
"""


def calculo(num1, num2, simbolo):
    if simbolo == '+':
        return num1 + num2
    elif simbolo == '-':
        return num1 - num2
    elif simbolo == '*':
        return num1 * num2
    elif simbolo == '/':
        return num1 / num2
    else:
        return 'Não foi possível realizar a operação. Operador inválido.'


print('+ para adição; - para subtração; * para multiplicação; / para divisão.')
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
operador = input("Operação a ser realizada: ")
print(calculo(numero1, numero2, operador))
