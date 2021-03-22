"""
Deseja-se converter uma medida de temperatura
da escala Celsius para Fahrenheit ou vice-versa.
Para isso, você deve construir um programa que
leia a letra "C" ou "F" indicando em qual escala
vai ser informada uma temperatura. Em seguida, o
programa deve mostrar a temperatura na outra escala
com duas casas decimais. A seguir é dada a fórmula
para converter de Fahrenheit para Celsius (você deve
deduzir a fórmula de Celsius para Fahrenheit):
C = (5/9) * (F - 32)
"""

escala = input("Você vai digitar a temperatura em qual escala (C/F)? ")

if escala == "C" or escala == "c":
    celsius = float(input("Digite a temperatura em Celsius: "))
    temperatura = celsius * 1.8 + 32
    print(f"Temperatura equivalente em Fahrenheit: {temperatura:.2f} ")
elif escala == "F" or escala == "f":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    temperatura = (5 * (fahrenheit - 32))/9
    print(f"Temperatura equivalente em Celsius: {temperatura:.2f}")
else:
    print("Valor inserido não é válido")
