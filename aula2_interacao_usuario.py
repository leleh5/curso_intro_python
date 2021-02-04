a = int(input('digite um valor inteiro'))
b = float(input('digite um valor decimal'))
soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b
resto = a%b
print('soma:', soma)
print('subtração: ' + str(subtracao))
print('multiplicação: {}' .format(multiplicacao))
print('divisão: {div}. \nresto: {rest}' .format(rest=resto, div=divisao))