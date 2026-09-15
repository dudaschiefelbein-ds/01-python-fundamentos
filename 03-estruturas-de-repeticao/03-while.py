continuar = True

while continuar:
    # Tudo aqui dentro pertence ao WHILE
    numero = int(input("Qual é a tabuada? "))
    
    for i in range(1, 11): 
        # Tudo aqui dentro pertence ao FOR
        print(f"{numero} x {i} = {numero * i}")
    
    # Esta parte saiu do FOR, mas continua dentro do WHILE
    continuar = input('Deseja continuar? (s/n) ')
    continuar = True if continuar == 's' else False
    
    #Aqui evoluimos o conceito fizemos dois loops um dentro do outro.