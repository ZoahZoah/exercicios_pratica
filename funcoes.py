def escolher_esporte(f, v, b, t):
    qnt_futebol = f
    qnt_volei = v
    qnt_basquete = b
    time_confianca = t
    letra_f = 'F'
    letra_v = 'V'
    letra_b = 'B'
    letras = False
    time = False

    print('-------------Bem-vindo(a) a nossa pesquisa-------------')
    print('Poderia nos responder qual o seu esporte favorito?')
    print('F - Futebol, V - Vôlei, B - Basquete')
    esporte_favorito = input('Digite a letra correspondente: ').upper()
    if (esporte_favorito == 'F'):
        letras = True
    elif (esporte_favorito == 'V'):
        letras = True
    elif (esporte_favorito == 'B'):
        letras = True
    print(esporte_favorito)

    while (letras == False):
        esporte_favorito = input('Por favor, digite a letra que corresponda as respostas: ').upper()
        if (esporte_favorito == 'F'):
            letras = True
        elif (esporte_favorito == 'V'):
            letras = True
        elif (esporte_favorito == 'B'):
            letras = True

    if (esporte_favorito == 'F'):
        qnt_futebol += 1
        time_favorito = input('Você torce para seu time de confiança? (S) ou (N): ').upper()
        while (not time):
            if (time_favorito == 'S'):
                time = time_favorito == 'S'
                time_confianca += 1

            else:
                time_favorito = input('Por favor, responda a pergunta. (S) ou (N): ').upper()

        print(f'Pessoas que gostam de futebol: {qnt_futebol}')
    elif (esporte_favorito == 'B'):
        qnt_basquete += 1
        print(f'Pessoas que gostam de basquete: {qnt_basquete}')
    else:
        qnt_volei += 1
        print(f'Pessoas que gostam de volei: {qnt_volei}')
    f = qnt_futebol
    v = qnt_volei
    b = qnt_basquete
    t = time_confianca
    return f, v, b, t


def escolher_genero(m, f, o):
    g_masculino = m
    g_feminino = f
    g_outro = o
    genero_bool = False

    print('Poderia nos responder qual o seu genero?')
    print('M - Masculino, F - Feminino, O - Outro')
    genero_candidato = input('Digite a letra correspondente: ').upper()
    print(genero_candidato)
    if (genero_candidato == 'M'):
        genero_bool = True
    elif (genero_candidato == 'F'):
        genero_bool = True
    elif (genero_candidato == 'O'):
        genero_bool = True

    while (genero_bool == False):
        genero_candidato = input('Por favor, digite a letra que corresponda as respostas: ').upper()
        if (genero_candidato == 'M'):
            genero_bool = True
        elif (genero_candidato == 'F'):
            genero_bool = True
        elif (genero_candidato == 'O'):
            genero_bool = True

    if (genero_candidato == ('M')):
        g_masculino = g_masculino + 1
        print(f'Pessoas gênero masculino que votaram: {g_masculino}')
    elif (genero_candidato == ('F')):
        g_feminino = g_feminino + 1
        print(f'Pessoas do gênero feminino que votaram: {g_feminino}')
    else:
        g_outro = g_outro + 1
        print(f'Pessoas de outro gênero que votaram: {g_outro}')
    m = g_masculino
    f = g_feminino
    o = g_outro
    return m, f, o

