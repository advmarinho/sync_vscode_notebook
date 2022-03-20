import pandas as pd
from numpy import append, indices, save, savetxt, sort

# pyinstaller --onefile --console .\aulaProjetoSplit.py

print('\n\033[1;33mSoftware para separar arquivos de texto em arquivos separados por palavras.\033[m')
print('\033[1;33mCriar um arquivo com nome texto.txt extraido do site e depois copiar o caminho e colar no input.\033[m')
print('\n\033[1;32mSoftware by Anderson Marinho \033[m')
print('\033[1;32mVersão 1.0 \033[m')
print('\n')

# arq = open('texto.txt', 'r', encoding="utf-8" )
abrir = input('\033[1;31mDigite caminho do arquivo: \033[m')
arq = open(abrir + '\\texto.txt', 'r', encoding="utf-8" )
string = arq.read()
lista0 = string.split(' ')  # split em palavras
# lista0 = set(string.split(' '))  # split em palavras
lista1 = (dict.fromkeys(string.split(' ')))  # split em palavras
# print(lista1)

palavras = []
for valor in lista1:
    valor = valor.replace(',','')
    valor = valor.replace('.','')
    valor = valor.replace(':','')
    valor = valor.replace(';','')
    valor = valor.replace('—','')
    valor = valor.replace(' ','')
    valor = valor.replace('?','')
    valor = valor.replace('!','')
    valor = valor.replace('“','')
    valor = valor.replace('–','')
    valor = valor.replace('“‘','')
    valor = valor.replace('“‘','')
    valor = valor.replace('”','')
    valor = valor.replace(')','')
    valor = valor.replace('(','')
    valor = valor.replace('‘','')
    # print(list(valor.strip().upper()))
    # print((valor.strip().upper()))
    valor = valor.strip().upper()
    palavras.append(valor)
    
print(palavras)
# salvar = input(r'Digite Caminho para Salvar: ')
savetxt(abrir + '\\palavras.csv', palavras, delimiter=';', fmt='%s')

abrirCSV = (abrir + '\\palavras.csv')

baseDados = pd.read_csv(abrirCSV, sep=';', low_memory=False, encoding='latin-1')
baseDados = baseDados.sort_values('COLUNA', ascending=True)
baseDados = baseDados.drop_duplicates(subset='COLUNA', keep='first')
baseDados = baseDados.reset_index(drop=True, inplace=False)
# baseDados.to_csv(input('Digite o nome do arquivo: ') +'.csv', sep=';', index=False, encoding='latin-1')
baseDados.count()
baseDados.to_csv(abrirCSV, sep=';', index=False, encoding='latin-1')


print(baseDados)
input('\n\033[1;31mPressione <ENTER> para sair.\033[m')
print('\033[1;31mFim do programa.\033[m')

