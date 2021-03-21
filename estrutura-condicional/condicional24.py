"""
Uma empresa vende o mesmo produto para quatro
diferentes estados. Cada estado possui uma taxa
diferente de imposto sobre o produto (MG 7%; SP
12%; RJ 15%; MS 8%). Faça um programa em que o
usuário entre com o valor e o estado destino do
produto e o programa retorne o preço final do
produto acrescido do imposto do estado em que
ele será vendido. Se o estado digitado não for
válido, mostrar uma mensagem de erro.
"""

print("Estados disponíveis: SP, RJ, MG, MS*")
print("*Consulte taxas de impostos")

valor = float(input("Digite o valor do produto: "))
estado = input("Digite o Estado para o qual o produto será enviado: ")

if estado == "SP" or estado == "sp":
    imposto = (valor * 12)/100
    print(f"Preço final (acrescido do imposto: {imposto + valor}")
elif estado == "RJ" or estado == "rj":
    imposto = (valor * 15)/100
    print(f"Preço final (acrescido do imposto: {imposto + valor}")
elif estado == "MG" or estado == "mg":
    imposto = (valor * 7)/100
    print(f"Preço final (acrescido do imposto: {imposto + valor}")
elif estado == "MS" or estado == "ms":
    imposto = (valor * 8)/100
    print(f"Preço final acrescido do imposto: {imposto + valor}")
else:
    print("Estado digitado não é elegível para envio")
