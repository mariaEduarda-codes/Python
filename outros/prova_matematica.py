"""
Faça uma prova de matemática para crianças que
estão aprendendo a somar números inteiros menores
do que 100. Escolha números aleatórios entre 1 e 100,
e mostre na tela a pergunta: qual é a soma de a + b,
onde a e b são números aleatórios. Peça a resposta.
Faça cinco perguntas ao aluno, e mostre para ele quantas
vezes ele acertou.
"""
import random

contagem = 0
perguntaa: [int] = [0 for x in range(100)]
perguntab: [int] = [0 for x in range(100)]
resposta: [int] = [0 for x in range(500)]

for i in range(0, 5):
    perguntaa = random.randint(0, 100)
    perguntab = random.randint(0, 100)
    resposta = int(input(f"{perguntaa} + {perguntab} =  "))
    if resposta == (perguntaa + perguntab):
        contagem += 1

print()
print(f"Acertos: {contagem}/5")
