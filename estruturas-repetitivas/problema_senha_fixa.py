"""
Escreva um programa que repita a leitura de uma senha até que ela
seja válida. Para cada leitura de senha incorreta informada, escrever
a mensagem "Senha Inválida! Tente novamente: ". Quando a senha for
informada corretamente deve ser impressa a mensagem "Acesso Permitido"
e o algoritmo encerrado. Considere que a senha correta é o valor 2002.
"""
senha = int(input("Digite a senha: "))

while senha != 2002:
    senha = int(input("Senha inválida! Tente novamente: "))
    if senha == 2002:
        print("Acesso permitido!")
