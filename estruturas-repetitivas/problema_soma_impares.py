"""
Leia 2 valores inteiros X e Y (em qualquer ordem).
A seguir, calcule e mostre a soma dos números
ímpares entre eles.
"""
print("Digite dois números: ")
x = int(input())
y = int(input())

if x > y:
    troca = x
    x = y
    y = troca

soma = 0
for i in range(x+1, y):
    if i % 2 != 0:
        soma += i

print(f"SOMA DOS ÍMPARES = {soma}")
