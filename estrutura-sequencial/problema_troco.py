"""
Fazer um programa para calcular o troco no processo de pagamento
de um produto de uma mercearia. O programa deve ler o preço unitário
do produto, a quantidade de unidades compradas deste produto, e o valor
em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu
programa deve mostrar o valor do troco a ser devolvido ao cliente.
"""
unitario = float(input("Preço unitário do produto: "))
qtd = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))
print(f"TROCO = {dinheiro - (unitario * qtd):.2f}")
