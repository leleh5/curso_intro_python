conjunto_a = {'a', 'b', 'c'}
conjunto_b = {'a', 'b', 'c', 'd', 'e'}

conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

lista = ['cachorro', 'gato', 'elefante', 'gato', 'papagaio']
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)

# conjunto1 = {1, 2, 3, 4, 5}
# conjunto2 = {5, 6, 7, 8, 9}
# conjunto1.add(185)
# conjunto1.discard(185)
#
# print(conjunto1,'\n',conjunto2)
#
# conjunto_uniao = conjunto1.union(conjunto2)
# conjunto_interseccao = conjunto1.intersection(conjunto2)
#
# print(conjunto_uniao,'\n',conjunto_interseccao)
#
# conjunto_diferenca1 = conjunto1.difference(conjunto2)
# conjunto_diferenca2 = conjunto2.difference(conjunto1)
#
# print('conjunto diferença 1 para 2: {}.\nconjunto diferença 2 para 1: {}.'.format(conjunto_diferenca1, conjunto_diferenca2))
#
# conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
#
# print('conjunto da diferença simétrica: {}'.format(conjunto_diff_simetrica))


