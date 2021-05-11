"""
Faça um programa que tenha uma função chamada escreva(), que recebe
um texto qualquer como parâmetro e mostra uma mensagem com tamanho
adaptável.
"""


def escreva(texto):
    tamanho = len(texto)
    print('~' * tamanho)
    print(texto)
    print('~' * tamanho)


escreva('Madu')
escreva('Maria Eduarda')
escreva('Maria Eduarda de Medeiros Lima Siqueira')
