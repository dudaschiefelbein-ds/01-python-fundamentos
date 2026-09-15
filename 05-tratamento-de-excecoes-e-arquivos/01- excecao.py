'''
try:
    n1= int (input('Número 1 é:'))
    n2= int (input('Número 2 é:'))

    resultado= n1 / n2 
    print(f"O resultado da divisão é:{resultado}")

except Exception as erro:                 
     print(f"Ocorreu um erro:{erro}")
    
     # O Exception é um erro genérico: pega QUALQUER erro que acontecer.
'''
     
try:
    n1= int (input('Número 1 é:'))
    n2= int (input('Número 2 é:'))
   
    resultado= n1 / n2 
    print(f"O resultado da divisão é:{resultado}")
     
except ValueError:
    # Quando o usuário digita letras em vez de números
    print("Favor digitar somente numeros")

except ZeroDivisionError:
    # Quando tenta dividir por zero
    print("Não é possivel dividir um número por 0")
    
except Exception as erro:
    # Qualquer outro erro que não seja os de cima
    print("ocorreu um erro: ", erro)

else:
    # Só roda se NÃO deu nenhum erro
    print("o programa foi executado corretamente") 

finally:
    # Roda SEMPRE no final (dando erro ou não)
    print("Fim.")