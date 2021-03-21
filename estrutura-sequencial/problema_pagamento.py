"""
Fazer um programa para ler o nome de um(a) funcionário(a),
o valor que ele(a) recebe por hora, e a quantidade de horas
trabalhadas por ele(a). Ao final, mostrar o valor do pagamento
do funcionário com uma mensagem explicativa.
"""

nome = input("Nome: ")
valor_hora = float(input("Valor por hora: "))
horas_trab = int(input("Horas trabalhadas: "))
print(f"O pagamento para {nome} deve ser {valor_hora * horas_trab:.2f}")
