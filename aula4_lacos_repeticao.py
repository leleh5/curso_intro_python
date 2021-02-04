# a = int(input('digite um número: '))
# div = 0
#
# for x in range(1, a+1):
#     resto = a % x
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('O número {} é primo.'.format(a))
#
# else:
#     print('O número {} não é primo.'.format(a))

# Números primos de 0 a 100:
# for a in range(101):
#     div = 0
#     for x in range(1, a+1):
#         resto = a % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print('{} é um número primo.'.format(a))

# Notas:
media = 0
for i in range(1, 5):
    nota = int(input('Nota {}: '.format(i)))
    while nota > 10:
        print('nota inválida.')
        nota = int(input('Nota {}: '.format(i)))
    media += nota
print('Média: {}'.format(media/4))
