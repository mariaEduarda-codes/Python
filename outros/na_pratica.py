"""
Ler valor de custo do couro
Ler valor de custo do solado
Ler valor de custo dos cordões e ilhoses
Ler valor de insumos
Ler valor de custo de mão de obra
Ler valor de custo de marketing
Ler valor de custo de vendas

Calcular preço de custo: (couro) x 30% + (solado) x 20% +
(cordões) x 5% + (insumos) x 5% + (mão de obra) x 20% +
(marketing) x 10% + (vendas) x 10%

Calcular o preço com lucro do fabricante: (preço de custo) x 1.30
Calcular preço com perdas de capital: (preço com lucro) x 1.15
Calcular preço com impostos federais IPI e COFINS (preço com perdas de
capital) x 1.15
Calcular preço com margem de vendas (preço IPI e COFINS) x 1.25
Calcular preço com impostos estaduais e municipais (preço margem e vendas) x 1.30
Preço final = preço com impostos estaduais e municipais
Apresentar em tela o preço de custo e preço final calculados
"""

couro = float(input("Custo do couro: "))
solado = float(input("Custo do solado: "))
cor_ilh = float(input("Custo dos cordões e ilhoses: "))
insumos = float(input("Valor de insumos: "))
mdo = float(input("Custo de mão de obra: "))
mkt = float(input("Custo de marketing: "))
vendas = float(input("Custo de vendas: "))

custo = (couro * 0.3) + (solado * 0.2) + (cor_ilh * 0.05) + (insumos * 0.05) + (mdo * 0.2) + (mkt * 0.1) + (vendas * 0.1)
lucro = custo * 1.30
perdas_capital = lucro * 1.15
impostos = perdas_capital * 1.15
mrg_vendas = impostos * 1.25
imp_est_mun = mrg_vendas * 1.30
preco_final = imp_est_mun

print(f"Preço de custo: {custo}")
print(f"Preço final: {preco_final:.2f}")
