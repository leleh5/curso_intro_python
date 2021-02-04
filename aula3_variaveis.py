# a = int(input('primeiro número: '))
# b = int(input('segundo número: '))
# c = int(input('terceiro número: '))
#
# if a>b and a>c:
#     print('{} é o maior número'.format(a))
#
# elif b>a and b>c:
#     print('{} é o maior número'.format(b))
#
# else:
#     print('{} é p maior número'.format(c))

# a = int(input('primeiro número: '))
# b = int(input('segundo número: '))
# c = int(input('terceiro número: '))
#
# if a>b:
#     aux = b
#     b = a
#     a = aux
#
# if b>c:
#     aux = c
#     c = b
#     b = aux
#
# if a>b:
#     aux = b
#     b = a
#     a = aux
#
# print(a, b, c)

# a = float(input('Número: '))
# b = float(input('Número: '))
#
# resto_a = a%2
# resto_b = b%2
#
# if resto_a==0 or not resto_b!=0:
#     print('pelo menos um número par foi digitado')

a = float(input('primeira nota: '))
if a>10:
    a = float(input('Nota digitada incorretamente. \nprimeira nota: '))

b = float(input('segunda nota: '))
if b>10:
    b = float(input('Nota digitada incorretamente. \nsegunda nota: '))

c = float(input('terceira nota: '))
if c>10:
    c = float(input('Nota digitada incorretamente. \nterceira nota: '))

d = float(input('quarta nota: '))
if d>10:
    d = float(input('Nota digitada incorretamente. \nquarta nota: '))

media = (a+b+c+d)/4
print('média: {}'.format(media))

