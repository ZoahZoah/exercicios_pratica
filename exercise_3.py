alunos = 10
primeiro_semestre = 0
segundo_semestre = 0
outro_semestre = 0
python_preferido = 0
java_preferido = 0
outras_preferido = 0
prefere_primeiro_ano = 0
fundamento_programacao = 0
projeto_software = 0

for aluno in range(1, alunos + 1):
    print('Aluno: ', aluno)
    melhor_disciplina = input(
        'A melhor disciplina: (FP) Fundamentos da Programação, (PS) Projetos de Software: ').upper()
    while (True):
        if (melhor_disciplina == 'FP'):
            fundamento_programacao += 1
            break
        elif (melhor_disciplina == 'PS'):
            projeto_software += 1
            break
        else:
            melhor_disciplina = input(
                'Por favor, digite as letras correspondentes: (FP) Fundamentos da Programação, (PS) Projetos de Software').upper()
    melhor_periodo = int(input(
        'Digite o número corresponde ao melhor período que você cursou (do 1º ao 8º: '))
    while (melhor_periodo < 1 and melhor_periodo > 8):
        melhor_periodo = int(input(
            'Digite o número corresponde ao melhor período que você cursou (do 1º ao 8º: '))
    if (melhor_periodo == 1):
        primeiro_semestre += 1
    elif (melhor_periodo == 2):
        segundo_semestre += 1
    else:
        outro_semestre += 1
    linguagem_preferida = input('Informe sua linguagem favorita: (P) Python, (J) Java, (O) Outros: ').upper()
    while (True):
        if (linguagem_preferida == 'P'):
            python_preferido += 1
            break
        elif (linguagem_preferida == 'J'):
            java_preferido += 1
            break
        elif (linguagem_preferida == 'O'):
            outras_preferido += 1
            break
        else:
            linguagem_preferida = input('Informe sua linguagem favorita: (P) Python, (J) Java, (O) Outros: ').upper()
    if (melhor_periodo == 1 or melhor_periodo == 2):
        prefere_primeiro_ano += 1

porcentual_primeiro_ano = (prefere_primeiro_ano * 100) / alunos
percentual_disciplina_fp = (fundamento_programacao * 100 ) / alunos
percentual_java_dislike = 100 - (java_preferido * 100) / alunos
print(f'O percentual de alunos que preferem java é: {porcentual_primeiro_ano}%.')
print(f'O porcentual de alunos que preferem fundamentos da programação é: {percentual_disciplina_fp}%.')
print(f'O porcental de alunos que não gostam de Java é: {percentual_java_dislike}%.')