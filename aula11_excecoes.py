lista = [1, 10]

try:
    arquivo = open('notas.txt', 'r')
    texto = arquivo.read()
    divisao = 1/0
    #numero = lista[3]
    #x = a
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except BaseException as ex:
    print('Erro: {}'.format(ex))
else:
    print('Executa quando não houverem exceptions')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
