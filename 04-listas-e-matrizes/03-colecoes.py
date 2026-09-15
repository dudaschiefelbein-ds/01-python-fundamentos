# ==========================================
# 1. CONJUNTOS
# ==========================================
conjunto = set([4, 7, 3, 0, 8])

# A diferença de uma lista para um conjunto é que o conjunto não aceita valores duplicados e não tem ordem.
# Eu não posso alterar um valor que já está lá dentro, mas posso adicionar ou remover itens. 
print("Conjuntos:", conjunto) 

'''
# Se eu der um print no conjunto, vocês vão observar que, quando eu mando imprimir, 
# ele é representado por chaves, não por colchetes. Então, se eu tiver chaves, é um conjunto.
'''

# ==========================================
# 2. TUPLAS
# ==========================================
tupla = (3, 2, 4, 6, 0)
print("tupla:", tupla)

'''
[ 1, 2, 3 ]  --> LISTA      [] (Usa colchetes. Maleável, muda tudo, tem ordem, aceita repetidos.)
{ 1, 2, 3 }  --> CONJUNTO   {} (Usa chaves. Não repete, não tem ordem, adiciona/remove)
( 1, 2, 3 )  --> TUPLA      () (Usa parênteses. Totalmente trancada, imutável, tem ordem)

Agora você já conhece as três principais coleções do Python:
'''

# ==========================================
# 3. DICIONÁRIOS EM PYTHON
# ==========================================

# '''
# A diferença de lista para dicionário: aqui, quantas informações de cada pessoa eu tenho? 
# Eu sei que tenho três pessoas diferentes, porém de cada pessoa eu tenho uma única informação: o nome.
# '''
# pessoas = ['Gui', 'Maria', 'João']
# print(pessoas)

# O dicionário serve para criar várias informações da mesma pessoa:
pessoa = {'Nome': 'Gui', 'Telefone': '(61) 98765 4321', 'Endereco': 'ABC'} 

print(pessoa['Nome'])      # Aqui se eu quiser o nome:
print(pessoa['Telefone'])  # Aqui se eu quiser o telefone:
print(pessoa['Endereco'])  # Aqui se eu quiser o endereço:

'''
Quantas variáveis eu tenho? Uma única variável. Quantas pessoas eu tenho nessa variável? Uma pessoa.
Diferentemente da lista, onde a vírgula separa itens diferentes (Gui, Maria e João, três pessoas),
aqui eu tenho uma única pessoa com vários atributos: nome, telefone, endereço.
'''

# ==========================================
# 4. LISTA DE DICIONÁRIOS
# ==========================================
pessoas = [
    {'Nome': 'Gui', 'Telefone': '(61) 98765 4321', 'Endereco': 'ABC'},          # Posição 0
    {'Nome': 'Maria', 'Telefone': '(62) 98765 4021', 'Endereco': 'DEF'},        # Posição 1
    {'Nome': 'João', 'Telefone': '(63) 98765 2020', 'Endereco': 'AAA'},         # Posição 2
    {'Nome': 'Antônio', 'Telefone': '(64) 98765 4321', 'Endereco': 'BBB'},      # Posição 3
]

print(pessoas)             # Aqui exibe todas pessoas
print(pessoas[0])          # Aqui exibe pessoas no indice zero só aparece a primeira pessoa
print(pessoas[0]['Nome'])  # Aqui se eu quiser exibir só o nome da pessoa
print(pessoas[2]['Telefone']) # Aqui exibir o telefone da posição 2