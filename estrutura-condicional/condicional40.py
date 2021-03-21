"""
O custo ao consumidor de um carro novo é
a soma do custo de fábrica, da comissão
do distribuidor, e dos impostos. A comissão
e os impostos são calculados sobre o custo
de fábrica, de acordo com a tabela abaixo.
Leia o custo de fábrica e escreva o custo
ao consumidor.

CUSTO DE FÁBRICA                    % DO DISTRIBUIDOR       % DOS IMPOSTOS
até R$12.000,00                         5                       isento
entre R$12.000,00 e 25.000,00           10                      15
acima de R$25.000,00                    15                      20
"""

custo_fabrica = float(input("Digite o custo de fábrica: "))

if custo_fabrica < 12_000:
    pt_distrib = (custo_fabrica * 5) / 100
    pt_impost = (0 * custo_fabrica) / 100
    custo_consumidor = custo_fabrica + pt_distrib + pt_impost
    print(f"Custo ao consumidor: {custo_consumidor}")
elif (custo_fabrica >= 12_000) and (custo_fabrica <= 25_000):
    pt_distrib = (custo_fabrica * 10) / 100
    pt_impost = (15 * custo_fabrica) / 100
    custo_consumidor = custo_fabrica + pt_distrib + pt_impost
    print(f"Custo ao consumidor: {custo_consumidor}")
else:
    pt_distrib = (custo_fabrica * 15) / 100
    pt_impost = (20 * custo_fabrica) / 100
    custo_consumidor = custo_fabrica + pt_distrib + pt_impost
    print(f"Custo ao consumidor: {custo_consumidor}")
