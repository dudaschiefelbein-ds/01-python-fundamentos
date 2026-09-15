numeros=[
  [ 3, 4, 7, 8 ], 
  [ 1, 3, 6, 2 ],   #Matrizes,(Tenho uma lista aonde cada posição da lista é outra lista).
  [ 6, 9, 7, 82 ],        
  [ 7, 5, 0, 81 ],    
]

print (numeros [1][2]) 
#O 1° colchete indice pega a lista (a linha),e 2° colchete pega (a coluna),indice 2 numero 6.

# ---------------------------------------------------------------------------------------------------
# MAPEAMENTO VISUAL DO COMETÁRIO:
#
#                       [Coluna 0] [Coluna 1] [Coluna 2] [Coluna 3]
# numeros[0] (Linha 0) ->   3          4          7          8
# numeros[1] (Linha 1) ->   1          3       👉 6 👈       2   <-- [1° colchete][2° colchete]
# numeros[2] (Linha 2) ->   6          9          7         82
# numeros[3] (Linha 3) ->   7          5          0         81
# --------------------------------------------------------------------------------------------------


