#dia = input("Digite o número do dia da semana:")

dia = int(input("Digite o número do dia da semana:")) #Transforma o resultado em inteiro

'''if dia == 1:  #Sem previsar de aspas
    print("Domingo")
elif dia == 2:
    print("Segunda-Feira")
elif dia == 3:
    print("Terça-Feira")
elif dia == 4:
    print("Quarta-Feira")
elif dia == 5:
    print("Quinta-Feira")
elif dia == 6:
    print("Sexta-Feira")
elif dia == 7:
    print("Sabado")
else:
    print("Esse dia não existe") #caso tenha um dia 8 por exmplo vai dar essa mensagem.
'''
match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-Feira")
    case 3:
        print("Terça-Feira")
    case 4:
        print("Quarta-Feira")
    case 5:
        print("Quinta-Feira")
    case 6:
        print("Sexta-Feira")
    case 7:
        print("Sabado")
    case other:
        print("Esse dia não existe")
    