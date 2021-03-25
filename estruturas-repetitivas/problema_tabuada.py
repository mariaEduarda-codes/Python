"""
Ler um número inteiro N, daí mostrar na tela
a tabuada de N para 1 a 10, conforme exemplo.
"""

n = int(input("Deseja a tabuada para qual valor? "))

for i in range(0, 10):
    print(f"{n} x {i + 1} = {n * (i + 1)}")
