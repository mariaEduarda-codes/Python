"""
Escreva o menu de opções abaixo. Leia a opção do usuário
e execute a operação escolhida. Escreva uma mensagem de
erro se a opção for inválida.

Escolha a opção:
1 - Soma de 2 números
2 - Diferença entre 2 números (maior pelo menor)
3 - Produto entre 2 números
4 - Divisão entre 2 números (o denominador não pode ser 0)
"""

print("Escolha a opção: ")
print("1 - Soma de 2 números")
print("2 - Diferença entre 2 números (maior pelo menor")
print("3 - Produto entre 2 números")
print("4 - Divisão entre 2 números (o denominador não pode ser 0")

escolha = int(input("Digite sua escolha: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == 1:
    print(f"Soma: {num1 + num2}")
elif escolha == 2:
    if num1 > num2:
        print(f"Diferença: {num1 - num2}")
    else:
        print(f"Diferença: {num2 - num1}")
elif escolha == 3:
    print(f"Produto: {num1 * num2}")
elif escolha == 4:
    if num2 == 0:
        print("Número inválido")
    else:
        print(f"Divisão: {num1 / num2}")
else:
    print("Escolha inválida")
