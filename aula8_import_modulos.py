from aula7_classes import Televisao
from aula8_contador_letras import contador_letras, teste


if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    
    lista = ['cachorro', 'gato', 'elefante']
    print('total de letras, por palavra, da lista: {}'.format(contador_letras(lista)))

    print(teste())