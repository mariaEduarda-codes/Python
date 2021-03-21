"""
Fazer um programa para ler uma duração de tempo em segundos,
daí imprimir na tela esta duração no formato horas:minutos:segundos.
"""

duracao = int(input("Digite a duração em segundos: "))
hora = int(duracao/3600)
minuto = int((duracao % 3600)/60)
segundo = int(duracao % 3600 - (minuto * 60))
print(f"{hora}:{minuto}:{segundo}")
