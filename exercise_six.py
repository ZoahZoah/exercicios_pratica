vetor_m = []
vetor_a = []
nota_aprovado = []

print('Olá, hoje faremos um calculo com a média de oito alunos.')
aluno = 1
for i in range(8):
    while (True):
        media_aluno = float(input(f'Digite a nota do aluno {aluno} (de 0 a 10): '))
        if (media_aluno >= 0 and media_aluno <= 10):
            vetor_m.append(media_aluno)
            aluno += 1
            break
        else:
            print('Você digitou um valor inválido, por favor, digite novamente.')

for i in vetor_m:
    nota = i
    if (nota > 6):
        nota_aprovado.append(i)

soma_notas = sum(nota_aprovado)
media_notas = soma_notas / len(nota_aprovado)
print(f'A media dos alunos aprovados foi: {media_notas}.')

for i in vetor_m:
    n = 0
    if (media_notas < i):
        vetor_a.append(n)
    n += 1

print(f'As notas dos alunos foram: {vetor_m}.')
print(f'Os indices respectivos aos alunos que obteram nota maior que a média dos aprovados foram: {vetor_a}.')