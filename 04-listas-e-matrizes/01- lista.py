# 4 Variáveis diferentes: n1, n2, n3, n4 
n1 = 10
n2 = 28
n3 = 38
n4 = 17

# Armazena uma variável com vários valores dentro dos colchetes
numeros = [10, 28, 38, 17, 57, 3, 7]  

# print(numeros)     # Se eu der um print, ele mostra exatamente como escrevi: [10, 28, 38, 17, 57, 3, 7].
# print(numeros[5])

# Posições (Índices): 0         1        2         3     4
carros =          ['Palio', 'Gol', 'Virtus', 'Ka', 'Onix']

# Exemplos de len(), append(), remove(), del, sorted()
# Exemplo: len() é usado para saber quantos itens tem na lista. Imprime/retorna.
# Vou numerar meus prints para organizar. Observe no terminal o retorno por transição.
         
print('1 ->', carros[2])  # Imprime 'Virtus' na posição 2.

# print(len(carros)) 

carros.append('Kombi')  # Adiciona Kombi na minha lista  
# print(len(carros))    # Ele imprime 6
print('2 ->', carros)   # Ele imprime ['Palio', 'Gol', 'Virtus', 'Ka', 'Onix', 'Kombi'] inserindo Kombi na minha lista

carros.remove('Gol')    # Quero remover um item utilizando o remove com o nome 'Gol' na minha lista
print('3 ->', carros)   # Como removi Gol, o Ka virou posição 2 e o Onix posição 3.

# Por isso abaixo, no quarto exemplo, ele remove o Onix na posição 3.
del carros[3]           # Removeu Onix
print('4 ->', carros) 

carros = sorted(carros)  # Isso aqui me retorna a lista de carros ordenada por nome. 
print('5 ->', carros)    
# Obs: no loop que vamos fazer, vai imprimir ordenado, se eu tirar a ordenação ele vai 
# imprimir os itens que estão  da lista original. caso queira tirar só comentar # carros = sorted(carros).

# Exibir um a um, os 4 carros na minha lista, cada um em uma linha.
print(carros[0])    # Carros posição zero
print(carros[1])    # Carros posição um 
print(carros[2])    # Carros posição dois
print(carros[3])    # Carros posição três

# Escrever um print(carros[ ]) para cada item funciona com 3 ou 4 carros. 
# O Problema ❌: Mas se a lista crescer para 14 ou 1.000, seu código fica gigante, repetitivo.
# A Solução (Loop for) 🚀: O for automatiza tudo, ele percorre a lista inteira e 
# imprime item por item, não importa se ela tem 5 ou 5.000 registros.

for carro in carros:
    print(carro)    
# Geralmente a gente usa a variável i. Como é fácil de confundir, melhor criar a variável carro(no singular)
# ... pois minha lista chama carros (no plural), então eu uso 'carro' no singular no loop (for).
 
 
 
 
 
 