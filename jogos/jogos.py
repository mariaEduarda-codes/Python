import jogo_forca
import jogo_adivinhacao

print("*******************************")
print("********Escolha seu jogo********")
print("*******************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo deseja jogar? "))

if jogo == 1:
    print("Jogando Forca")
    jogo_forca.jogar()
elif jogo == 2:
    print("Jogando Adivinhação")
    jogo_adivinhacao.jogar()
