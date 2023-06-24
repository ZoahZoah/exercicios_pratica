retangulo = 'R'
circulo = 'C'
quadrado = 'Q'
lado_ret = 0
altura_ret = 0
lado_quad = 0
raio_circ = 0
area_quadrado = 0
perimetro_quadrado = 0
area_retangulo = 0
perimetro_retangulo = 0
area_circulo = 0
perimetro_circulo = 0
numero_pi = 3.14

print('Olá, seja bem vindo ao programa que calcula área de figuras geométricas')
print('O programa trabalha com as seguintes figuras: ')
while (True):
    print('(R) Retangulo, (C) Círculo, (Q) Quadrado, (Z) Encerrar')
    figura_geometrica = input('Digite a letra da figura geométrica você deseja calcular a área: ').upper()
    if (figura_geometrica == retangulo):
        lado_ret = int(input('Digite o lado do retângulo: '))
        altura_ret = int(input('Digite a altura do retângulo: '))
        area_retangulo = lado_ret * altura_ret
        perimetro_retangulo = 2 * (lado_ret + altura_ret)
        print(f'A área do retângulo é {area_retangulo} e o perímetro é {perimetro_retangulo}.')
    elif (figura_geometrica == quadrado):
        lado_quad = int(input('Digite o lado do quadrado: '))
        area_quadrado = lado_quad ** 2
        perimetro_quadrado = lado_quad * 4
        print(f'A área do quadrado é {area_quadrado} e o perímetro é {perimetro_quadrado}.')
    elif (figura_geometrica == circulo):
        raio_circ = int(input('Digite o raio do círculo: '))
        area_circulo = numero_pi * (raio_circ ** 2)
        perimetro_circulo = 2 * numero_pi * raio_circ
        print(f'A área do circulo é {area_circulo} e o perímetro é {perimetro_circulo}.')
    elif (figura_geometrica == 'Z'):
        break
    else:
        print('Você digitou uma letra incorreta')

