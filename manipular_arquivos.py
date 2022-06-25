import os
import shutil

caminho_original = '/home/ubiratan/Pictures'
caminho_novo = '/home/ubiratan/Pictures2'

try:
    os.mkdir(caminho_novo) #função para criar uma nova pasta.
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
    
        shutil.move(old_file_path, new_file_path) #função para MOVER os arquivos para dentro do new file path.
        print(f'Arquivo {file} movido com sucesso')

        if '.jpeg' in file:
             shutil.copy(old_file_path, new_file_path) #função para COPIAR os arquivos .jpeg para dentro do new file path.
             print(f'Arquivo {file} copiado com sucesso')

        if '.jpeg' in file:
            os.remove(new_file_path) #função para DELETAR os arquivos .jpeg para dentro do new file path.
            print(f'Arquivo {file} deletado com sucesso.')
