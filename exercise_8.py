import random

vetor_int = []

for i in range(1000):
    numero_aleatorio = random.randrange(0, 21)
    vetor_int.append(numero_aleatorio)

for i in range(21):
    numero_aleatorio = vetor_int.count(i)
    print(f'O número {i} ocorreu {numero_aleatorio} vezes.')
