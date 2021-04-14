import random

print("*******************")
print("JOGO DA ADIVINHAÇÃO")
print("*******************")

numero_secreto = random.randint(0, 10)
chute = int(input("Qual é o número secreto? "))

if chute == numero_secreto:
    print("Você acertou!")
else:
    for tentativas in range(5, 0, -1):
        print(f"Você errou. Tente novamente. Tentativas restantes: {tentativas} ")
        chute = int(input("Qual é o número secreto? "))
        if tentativas == 1:
            print(f"Você perdeu! O número secreto era {numero_secreto}. ")
