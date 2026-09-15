import json #biblioteca json

pessoas = [
    {'Nome': 'Eduarda', 'Telefone': '(61) 98775-4321', 'Endereco': 'ABC'},  # Posição 0
    {'Nome': 'Maria',   'Telefone': '(62) 98765-4021', 'Endereco': 'DEF'},  # Posição 1
    {'Nome': 'Joao',    'Telefone': '(63) 98765-2020', 'Endereco': 'AAAB'}, # Posição 2
]

with open('pessoas.json', 'w') as arquivo:
       json.dump(pessoas, arquivo, indent=4) 
       # o Dump ele pega alguma coisa e joga dentro do meu arquivo.