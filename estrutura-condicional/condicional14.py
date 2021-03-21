"""
A nota final de um estudante é calculada a partir de três
notas atribuídas entre o intervalo de 0 até 10, respectivamente,
a um trabalho de laboratório, a uma avaliação semestral e a um
exame final. A média das três notas mencionadas anteriormente
obedece os pesos: Trabalho de Laboratório: 2; Avaliação Semestral:
3; Exame Final: 5. De acordo com o resultado, mostre na tela se
o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3
e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.
"""

nota1 = float(input("Digite a primeira nota (Trabalho de Laboratório): "))
nota2 = float(input("Digite a segunda nota (Avaliação Semestral): "))
nota3 = float(input("Digite a terceira nota (Exame Final): "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5)/(2 + 3 + 5)

if media == 0 or media <= 2.9:
    print("Reprovado")
elif 3 <= media <= 4.9:
    print("De recuperação")
elif 5 <= media <= 10:
    print("Aprovado")
