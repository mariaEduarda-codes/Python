"""
Leia a hora inicial e a hora final de um jogo. A seguir calcule
a duração do jogo, sabendo que o mesmo pode começar em um dia
e terminar em outro, tendo uma duração mínima de 1 hora e máxima
de 24 horas.
"""

inicial = int(input("Hora inicial: "))
final = int(input("Hora final: "))

if final > inicial:
    print(f"O jogo durou {final - inicial} hora(s)")
else:
    print(f"O jogo durou {24 - (inicial - final)} hora(s)")
