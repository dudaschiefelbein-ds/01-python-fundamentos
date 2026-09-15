for i in range(1, 11):          #variavel i
    print ()
    print ("Tabuada de {i}")    # esse aqui aparece uma vez o loop , que é o i
    for j in range (1, 11):     #variavel j
        print(f"{i} x {j}= {i * j}")   #Aqui aparece 10 x o loop (ele imprime 10 x o j)