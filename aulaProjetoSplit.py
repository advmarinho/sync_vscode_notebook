import pandas as pd
from numpy import append, indices, save, savetxt, sort

print('\nSoftware para separar arquivos de texto em arquivos separados por palavras.')
print('Criar um arquivo com nome texto.txt extraido do site e depois copiar o caminho e colar no input.')
print('Software by Andeson Marinho.\n')

# arq = open('texto.txt', 'r', encoding="utf-8" )
arq = open(input('Digite caminho do arquivo: ') + '\\texto.txt', 'r', encoding="utf-8" )
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
    # print(list(valor.strip().upper()))
    # print((valor.strip().upper()))
    valor = valor.strip().upper()
    palavras.append(valor)
    
print(palavras)
savetxt('palavras.csv', palavras, delimiter=';', fmt='%s')

abrirCSV = 'palavras.csv'
baseDados = pd.read_csv(abrirCSV, sep=';', low_memory=False, encoding='latin-1')
baseDados = baseDados.sort_values('UM', ascending=True)
baseDados = baseDados.drop_duplicates(subset='UM', keep='first')
baseDados = baseDados.reset_index(drop=True, inplace=False)
# baseDados.to_csv(input('Digite o nome do arquivo: ') +'.csv', sep=';', index=False, encoding='latin-1')
baseDados.to_csv(abrirCSV, sep=';', index=False, encoding='latin-1')


print(baseDados)
input('\nPressione <ENTER> para sair.')
print('Fim do programa.')

