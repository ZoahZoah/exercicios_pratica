import funcoes

pessoas_total = 0
futebol_favorito = 0
time_confianca = 0
torcida = 0
volei_favorito = 0
basquete_favorito = 0
c_masculino = 0
c_feminino = 0
c_outro = 0
mulheres_volei = 0
esporte_z = False

while (not esporte_z):
    esporte_x = False

    futebol_favorito, volei_favorito, basquete_favorito, time_confianca = funcoes.escolher_esporte(futebol_favorito, volei_favorito, basquete_favorito, time_confianca)
    c_masculino, c_feminino, c_outro = funcoes.escolher_genero(c_masculino, c_feminino, c_outro)

    pessoas_total += 1
    if (volei_favorito == 1 and c_feminino == 1):
        mulheres_volei += 1

    if (c_masculino == 1 and time_confianca == 1):
        torcida += 1

    escolha = input('Para continuar a pesquisa digite a letra "C" e para encerrar "Z": ').upper()
    while (not esporte_x):
        if (escolha == ('Z')):
            esporte_z = True
            esporte_x = True
        elif (escolha == ('C')):
            esporte_x = True
        else:
            escolha = input('Para continuar a pesquisa digite a letra "C" e para encerrar "Z": ').upper()

porcentagem_futebol = (futebol_favorito * 100) / pessoas_total
print(f'A porcentagem do total de pessoas que preferem futebol é: {porcentagem_futebol}%')
porcentagem_volei = (mulheres_volei * 100) / c_feminino
print(f'A porcentagem total de mulheres que preferem vôlei é: {porcentagem_volei}%')
torcida_fiel = (time_confianca * 100) / futebol_favorito
print(f'A porcentagem total de pessoas que torcem para o time de confiança no futebol é: {torcida_fiel}%')

