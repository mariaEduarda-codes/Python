"""
Faça um programa para ler um número indeterminado
de dados, contendo cada um, a idade de um indivíduo.
O último dado, que não entrará nos cálculos, contém
um valor de idade negativa. Calcular e imprimir a
idade média deste grupo de indivíduos. Se for entrado
um valor negativo na primeira vez, mostrar a mensagem
"IMPOSSÍVEL CALCULAR".
"""
print("Digite as idades: ")
idade = int(input())
soma = 0
contagem = 0

while idade > 0:
    soma += idade
    contagem += 1
    idade = int(input())

if idade < 0 and contagem == 0:
    print("IMPOSSÍVEL CALCULAR")
else:
    print(f"MÉDIA = {soma / contagem:.2f}")
