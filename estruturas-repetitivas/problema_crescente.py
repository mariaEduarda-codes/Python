"""
Leia uma quantidade indeterminada de duplas de
valores inteiros X e Y. Escreva para cada X e Y
uma mensagem que indique se estes valores foram
digitados em ordem crescente ou decrescente. O
programa deve finalizar quando forem digitados
dois valores iguais.
"""

print("Digite dois números: ")
a = int(input())
b = int(input())

while a != b:
    if a > b:
        print("Decrescente!")
    elif a < b:
        print("Crescente!")
    print("Digite dois números: ")
    a = int(input())
    b = int(input())
