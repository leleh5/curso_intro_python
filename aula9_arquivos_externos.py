import shutil

def escrever_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
    arquivo.close()

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        lista_media.append({aluno: media(lista_notas)})
    print(lista_media)

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/teste/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/teste/notas/notas_alunos.txt')

if __name__ == '__main__':
    #escrever_arquivo('notas.txt', 'Rafael: 10, 10, 5, 5\n')
    #atualizar_arquivo('notas.txt', 'Felipe: 5, 8, 6, 7\n')
    #ler_arquivo('notas.txt')
    #media_notas('notas.txt')
    #copia_arquivo('notas.txt')
    move_arquivo('C:/teste/notas.txt')


