

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def operar():
    a = float(input("Digite um número: "))
    b = float(input("Digite um número: "))

    print("+ para adição; - para subtração; * para multiplicação; / para divisão")
    operacao = input("Que operação deseja? ")
    if operacao == '+':
        print(somar(a, b))
    elif operacao == '-':
        print(subtrair(a, b))
    elif operacao == '*':
        print(multiplicar(a, b))
    elif operacao == '/':
        print(dividir(a, b))


operar()
