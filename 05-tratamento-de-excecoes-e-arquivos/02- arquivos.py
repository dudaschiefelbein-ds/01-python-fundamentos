# MODO TRADICIONAL (funciona, mas pode esquecer de fechar se der erro no código)
#arquivo= open('pessoas.txt', 'a+')
arquivo= open('pessoas.txt', 'w')
arquivo.write('Joao\n')
arquivo.write('Eduarda\n')
arquivo.write('Maria\n')
#  Enquanto eu não der esse close, o arquivo fica aberto,podendo dar problemas, 
# inclusive de eu tentar pegar esse arquivo, 
# que já deveria estar fechado, e fazer alguma outra coisa com ele.
arquivo.close()

#Completar com a instrução with resolve exatamente,
# esse problema de esquecer de fechar o arquivo!
#Posso usar a forma de cima (sem with) ou a forma de baixo (com with), 
# MODO RECOMENDADO (o 'with' fecha o arquivo automaticamente, sendo a opção mais segura)
with open('pessoas.txt', 'r+') as arquivoLeitura:
  for linha in arquivoLeitura:
     print(linha)