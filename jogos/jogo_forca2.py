palavra_secreta = 'otorrinolaringologista'
palavra_secreta = palavra_secreta.upper()
letras_acertadas = ['_' for letra in palavra_secreta]
print(f"A palavra é: {letras_acertadas}")

acertou = False
enforcou = False
tentativas = 6

while (not acertou) and (not enforcou):
    chute = input("Chuta uma letra: ")
    chute = chute.strip()
    index = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = chute.upper()
        index += 1

    print(letras_acertadas)

    if chute.upper() not in palavra_secreta.upper():
        tentativas -= 1
        print(f"Restam {tentativas} tentativas")
        if tentativas == 0:
            enforcou = True
            print("Você perdeu!")
            break

    if '_' not in letras_acertadas:
        acertou = True
        print("Você ganhou! ")
        break

# Jogo da forca, desta vez feito por mim, sem acompanhamento do instrutor.        
