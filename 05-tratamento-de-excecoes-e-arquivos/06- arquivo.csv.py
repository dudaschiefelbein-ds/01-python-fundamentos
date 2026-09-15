import csv

carros = [
['VW', 'Virtus', '2017'],
['VW', 'Gol', '1999'],
['Fiat', 'Palio', '2002'],
]

with open('carros.csv', 'w', newline='') as arquivo:
    fileCSV= csv.writer(arquivo, delimiter=';')
    fileCSV.writerow(['Marca', 'Modelo', 'Ano' ])   # Escreve o cabeçalho
    fileCSV.writerows(carros)                       # Escreve a lista de carros
    
    '''Ele vai criar o arquivo, escrever o cabeçalho com writerow e adicionar ,
    todas as linhas de dados com writerows.
    csv.writer(arquivo): Cria o "gravador" responsável por formatar os dados no padrão CSV.
writerow(...): Escreve uma única linha (ideal para o cabeçalho).
writerows(...): Escreve múltiplas linhas de uma vez só (passando uma lista de listas).
'''
'''1. Preparação dos Dados Criou a lista carros onde cada item é outra lista 
representando uma linha da tabela
(com Marca, Modelo e Ano). 
2. Manipulação do Arquivo (with open ...) open('carros.csv', 'w'): 
Abriu (ou criou) o arquivo carros.csv em modo de escrita ('w').  
csv.writer(arquivo): Criou o objeto gravador (fileCSV), 
que sabe converter listas do Python no formato CSV (separado por vírgulas).  
fileCSV.writerow(['Marca', 'Modelo', 'Ano']): Gravou o cabeçalho (uma única linha com o nome das colunas).
fileCSV.writerows(carros): Gravou todas as linhas da lista carros de uma só vez.'''