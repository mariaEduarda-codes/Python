import math
"""
Calcule as raizes da equação de 2º grau.
Lembrando que 
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
Onde
    delta = b ** 2 - (4 * a * c)
    
E ax² + bx + c = 0 representa uma equação de 2º grau

A variável a tem que ser diferente de 0. Caso seja igual,
imprima a mensagem "Não é equação do segundo grau". 

Se delta < 0, não existe raiz real. Imprima a mensagem "Não existe raiz"
Se delta = 0, existe uma raiz real. Imprima a raiz e a mensagem "Raiz única"
Se delta > 0, imprima as duas raízes reais
"""

print("Vamos calcular uma equação do segundo grau!")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - (4 * a * c)

if a != 0:
    if delta < 0:
        print("Não existe raiz real")
    elif delta == 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Raiz única {x1, x2}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"x1 = {x1} e x2 = {x2}")
else:
    print("Não é equação do segundo grau.")
