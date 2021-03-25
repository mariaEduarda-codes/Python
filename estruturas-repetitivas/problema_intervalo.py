"""
Leia um valor inteiro N. Este valor será
a quantidade de valores inteiros X que
serão lidos em seguida. Mostre quantos destes
valores X estão dentro do intervalo [10, 20] e
quantos estão fora do intervalo, conforme exemplo.
"""

n = int(input("Quantos números você vai digitar? "))
dentro_intervalo = 0
fora_intervalo = 0

for i in range(0, 5):
    x = int(input("Digite um número: "))
    if 10 >= x <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1

print(f"{dentro_intervalo} DENTRO DO INTERVALO [10, 20] ")
print(f"{fora_intervalo} FORA DO INTERVALO [10, 20] ")
