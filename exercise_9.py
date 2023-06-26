import random

numero_funcionarios = 10
funcionarios_idosos = 0
total_salario_funcionarios = 0
total_altura_idoso = 0
peso_minimo = 200
idade_minima = 90
salario_maior = 0
salario_minimo = 1320

for i in range(numero_funcionarios):
    idade = random.randrange(18, 90)
    print(f'Idade: {idade}', end='     ')
    salario = round(random.uniform(1320.00, 5000.00), 2)
    print(f'Salário: R${salario}', end='      ')
    peso_atual = random.randrange(40, 200)
    print(f'Peso: {peso_atual}', end='      ')
    altura = round(random.uniform(1.40, 2.00), 2)
    print(f'Altura: {altura}')

    total_salario_funcionarios += salario
    if (idade >= 65):
        funcionarios_idosos += 1
        total_altura_idoso += altura
    elif (idade < idade_minima):
        idade_minima = idade
        peso_minimo = peso_atual
    elif (salario > salario_maior):
        salario_maior = salario

media_salario = total_salario_funcionarios / numero_funcionarios
print(f'A média salarial dos funcionários é: R${media_salario}')

try:
    media_altura_idoso = round(total_altura_idoso / funcionarios_idosos, 2)
    print(f'A media de altura dos idosos é de: {media_altura_idoso}m')
except:
    ZeroDivisionError

print(f'A pessoa mais nova pesa: {peso_minimo}kg')

total_em_salario_minimo = round(salario_maior / salario_minimo, 2)
print(f'O maior salario convertido em salarios minimos é de: {total_em_salario_minimo} salarios mínimos')

multiplos_idade_ate_200 = range(idade_minima, 200, idade_minima)
print(f'Multiplos de: {idade_minima}')
for i in multiplos_idade_ate_200:
      print(f'{i}', end=',  ')

