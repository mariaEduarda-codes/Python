"""
Faça um programa que some os números ímpares em um intervalo definido pelo 
usuário. O usuário define o valor inicial e o valor final desse 
intervalo e o programa deve somar todos os ímpares neste intervalo.
Caso o usuário digite um valor inválido(começando pelo valor maior
que o final), deve ser escrito uma mensagem de erro na tela e o
programa termina.
"""

valor_inicial = int(input('Digite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))
impares = []

if valor_inicial > valor_final:
    print('Valor inicial deve ser menor que o valor final')
else:
    for numero in range(valor_inicial, valor_final):
        if numero % 2 != 0:
            impares.append(numero)
    soma = sum(impares)
    print(f'A soma dos ímpares no intervalo de {valor_inicial} a {valor_final} é {soma}')

