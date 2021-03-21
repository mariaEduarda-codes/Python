"""
Faça um programa que leia três números inteiros
positivos e efetue o cálculo de uma das seguintes
médias de acordo com um valor numérico digitado
pelo usuário.

(a) Geométrica: Raiz cúbica de x * y * z
(b) Ponderada: (x + 2*y + 3*z)/6
(c) Harmônica: 1/(1/x + 1/y + 1/z)
(d) Aritmética: (x + y + z)/3
"""
print("(a) Média geométrica")
print("(b) Média Ponderada")
print("(c) Média Harmônica")
print("(d) Média Aritmética")

escolha = input("Escolha um cálculo de média: ")
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))

geometrica = (x * y * z) ** (1/3)
ponderada = (x + 2 * y + 3 * z)/6
harmonica = 1/(1/x + 1/y + 1/z)
aritmetica = (x + y + z)/3

if (x or y or z) <= 0:
    print("Apenas números inteiros positivos permitidos")
elif escolha == "a" or escolha == "A":
    print(f"Média geométrica: {geometrica}")
elif escolha == "b" or escolha == "B":
    print(f"Média ponderada: {ponderada}")
elif escolha == "c" or escolha == "C":
    print(f"Média harmônica: {harmonica}")
elif escolha == "d" or escolha == "D":
    print(f"Média aritmética: {aritmetica}")
else:
    print("Escolha não válida")
