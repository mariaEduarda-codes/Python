"""
Usando switch, escreva um programa que leia um inteiro entre
1 e 7 e imprima o dia da semana correspondente a este número.
Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
"""
# Falaram que Python não tem switch então vou fazer sem mesmo

numero = int(input("Digite um inteiro entre 1 e 7: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda")
elif numero == 3:
    print("Terça")
elif numero == 4:
    print("Quarta")
elif numero == 5:
    print("Quinta")
elif numero == 6:
    print("Sexta")
elif numero == 7:
    print("Sábado")
else:
    print("Número inválido")
