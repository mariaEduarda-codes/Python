"""
Leia o salário de um trabalhador e o valor da prestação de
um empréstimo. Se a prestação for maior que 20% do salário
imprima: Empréstimo não concedido, caso contrário, imprima
Empréstimo concedido.
"""

salario = float(input("Digite o salário: "))
emprestimo = float(input("Digite o valor da prestação do empréstimo: "))

porcentagem = (20*salario)/100

if emprestimo > porcentagem:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido")
