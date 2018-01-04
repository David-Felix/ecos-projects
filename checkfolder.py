# encoding: utf-8
# -----------------------------------#
# Program: checkfolder.py
# Date: Wednesday, January 03, 2018
# @uthor: David Félix
# e-mail: davidfelixjt@hotmail.com
# -----------------------------------#

# Imports
import os

# Variáveis globais
E = '\e' # Gambiarra temporária, serve para adicionar a \ antes da pasta da escola

# Diretórios que contém os arquivos a serão comparados
MAIN_FOLDER = "C:\Users\Oficial\Desktop\chamados"
SCHOOLS_FOLDER = "C:\Users\Oficial\Desktop\escolas"

# Listas de pastas das escolas contidas nos diretórios
main_directory_list = os.listdir(MAIN_FOLDER)
schools_directory_list = os.listdir(SCHOOLS_FOLDER)

# Percorre os arquivos contidos nas pastas das escolas
for folder in main_directory_list:

    # Remove a primeira letra E do nome da escola e substitui pela variável global E(\e)
    aux_folder = folder.replace(folder[0],"")

    # Guarda os arquivos da pasta corrente em uma lista
    files_from_folder = os.listdir(MAIN_FOLDER + E + aux_folder)

    for schools_folders in schools_directory_list:

        aux_folder = schools_folders.replace(schools_folders[0],"")

        files_from_schools_folder = os.listdir(SCHOOLS_FOLDER + E + aux_folder)

        break

    print '\nComparação'
    print 'Pasta em Chamados: ' + folder
    print 'Quantidade de arquivos: ' + str(len(files_from_folder))
    print 'Pasta em Escolas: ' + schools_folders
    print 'Quantidade de arquivos: ' + str(len(files_from_schools_folder))
    print '\n'





