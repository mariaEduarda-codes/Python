"""
Uma lanchonete possui vários produtos. Cada produto possui um
código e um preço. Você deve fazer um programa para ler o código
e a quantidade comprada de um produto (suponha um código válido),
e daí informar qual o valor a ser pago, com duas casas decimais,
conforme tabela de produtos abaixo.

CÓDIGO      PREÇO DO PRODUTO
1           R$5.00
2           R$3.50
3           R$4.80
4           R$8.90
5           R$7.32
"""
codigo = int(input("Código do produto comprado: "))
qtd = int(input("Quantidade comprada: "))

if codigo == 1:
    valor = 5.00
elif codigo == 2:
    valor = 3.50
elif codigo == 3:
    valor = 4.80
elif codigo == 4:
    valor = 8.90
elif codigo == 5:
    valor = 7.32
else:
    print("Código inválido")

print(f"Valor a pagar: R$ {qtd * valor:.2f}")
