"""
Fazer um programa para calcular o troco no processo
de pagamento de um produto de uma mercearia. O programa
deve ler o preço unitário do produto, a quantidade de unidades
compradas deste produto, e o valor em dinheiro dado pelo cliente.
Seu programa deve mostrar o valor do troco a ser devolvido ao cliente.
Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem
informado o valor restante.
"""

unitario = float(input("Preço unitário do produto: "))
qtd = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

total = unitario * qtd

if dinheiro > total:
    print(f"TROCO = {dinheiro - total:.2f}")
else:
    print(f"DINHEIRO INSUFICIENTE. FALTAM {total - dinheiro:.2f} REAIS")
