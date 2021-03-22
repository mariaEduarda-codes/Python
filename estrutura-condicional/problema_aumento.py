"""
Uma empresa vai conceder um aumento percentual de
salário aos seus funcionários dependendo de quanto
cada pessoa ganha, conforme tabela ao lado. Fazer
um programa para ler o salário de uma pessoa, daí
mostrar qual o novo salário desta pessoa depois do
aumento, quanto foi o aumento e qual foi a porcentagem
de aumento.

Salário atual           Aumento
Até R$ 1000.00             20%

Acima de R$ 1000.00
até R$ 3000.00             15%

Acima de R$ 3000.00
até R$ 8000.00             10%

Acima de R$ 8000.00         5%
"""
salario = float(input("Digite o salário da pessoa: "))

if salario <= 1000:
    aumento = 0.2
    porcentagem = 20
    novo_salario = salario + (salario * aumento)
elif (salario > 1000) and salario <= 3000:
    aumento = 0.15
    porcentagem = 15
    novo_salario = salario + (salario * aumento)
elif (salario > 3000) and salario <= 8000:
    aumento = 0.1
    porcentagem = 10
    novo_salario = salario + (salario * aumento)
else:
    aumento = 0.05
    porcentagem = 5
    novo_salario = salario + (salario * aumento)

print(f"Novo salário = R$ {novo_salario:.2f}")
print(f"Aumento = R$ {salario * aumento:.2f}")
print(f"Porcentagem = {porcentagem} %")
