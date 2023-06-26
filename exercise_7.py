vetor_v = []
vetor_p = []
vetor_i = []
vetor_ap = []
vetor_ai = []

for i in range(10):
   while (True):
      idade_aluno = int(input(f'Digite a idade do aluno {i + 1}: '))
      if (6 <= idade_aluno <= 100):
         vetor_v.append(idade_aluno)
         if ((idade_aluno % 2) == 0):
            vetor_p.append(idade_aluno)
         else:
            vetor_i.append(idade_aluno)
         break
      else:
         print('Idade incorreta, por favor digite um valor válido (entre 6 e 100).')

for i in vetor_p:
   if (i > 18):
      vetor_ap.append(i)

for i in vetor_i:
   if (i > 18):
      vetor_ai.append(i)

print(vetor_v)
print(vetor_p)
print(vetor_i)
print(vetor_ap)
print(vetor_ai)