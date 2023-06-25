import random

valores_inteiros = 30
vetores_30 = []

for vetor in range(valores_inteiros):
    vetores_30.append(random.randrange(0, 50))

numero_informado = int(input('Informe um número de 0 a 50: '))
while True:
    if (numero_informado < 0 or numero_informado > 50):
        numero_informado = int(input('Informe um número de 0 a 50: '))
    else:
        break

numero_repetido = vetores_30.count(numero_informado)
print(numero_repetido)