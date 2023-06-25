

while (True):
    numero_sorteado = int(input('Digite um numero entre 1000 e 9999: '))
    if (numero_sorteado < 1000 or numero_sorteado > 9999):
        print('Numero inválido. Tente novamente.')
    else:
        break

milhar = numero_sorteado // 1000
centena = (numero_sorteado % 1000) // 100
dezena = (numero_sorteado % 100) // 10
unidade = numero_sorteado % 10

unidades_contagem = [milhar, centena, dezena, unidade]
print(unidades_contagem)