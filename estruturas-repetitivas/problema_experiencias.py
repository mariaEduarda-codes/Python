"""
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa
de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável.
Ela quer saber no final do ano, quantas cobais foram utilizadas no laboratório e o
percentual de cada tipo de cobaia utilizada. Este laboratório em especial utiliza
três tipos de cobais: sapos, ratos e coelhos. Para obter estas informações, ela
sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa
que leia um valor inteiro N que indica os vários casos de teste que vem a seguir.
Cada caso de teste contém um inteiro que representa a quantidade de cobaias utilizadas
e uma letra ('C', 'R' ou 'S'), indicando o tipo de cobaia (R: Rato; S: Sapo; C: Coelho).
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o
percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual
deve ser apresentado com dois dígitos após o ponto.
"""

casos = int(input("Quantos casos de teste serão digitados? "))
total_cobaias = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0

for i in range(0, casos):
    qtd_cobaias = int(input("Quantidade de cobaias: "))
    total_cobaias += qtd_cobaias
    tipo_cobaias = str(input("Tipo de cobaia: "))
    if (tipo_cobaias == 'C') or (tipo_cobaias == 'c'):
        total_coelhos += qtd_cobaias
    elif (tipo_cobaias == 'R') or (tipo_cobaias == 'r'):
        total_ratos += qtd_cobaias
    elif (tipo_cobaias == 'S') or (tipo_cobaias == 's'):
        total_sapos += qtd_cobaias

percent_coelhos = (total_coelhos * 100)/total_cobaias
percent_ratos = (total_ratos * 100)/total_cobaias
percent_sapos = (total_sapos * 100)/total_cobaias

print()
print("RELATÓRIO FINAL: ")
print(f"TOTAL = {total_cobaias} cobaias")
print(f"TOTAL DE COELHOS = {total_coelhos}")
print(f"TOTAL DE RATOS = {total_ratos}")
print(f"TOTAL DE SAPOS = {total_sapos}")
print(f"PERCENTUAL DE COELHOS = {percent_coelhos:.2f}")
print(f"PERCENTUAL DE RATOS = {percent_ratos:.2f}")
print(f"PERCENTUAL DE SAPOS = {percent_sapos:.2f}")
