"""
Se desea resolver el siguiente problema: dado el mismo tablero de 7x7, llenar el tablero de reyes y soldados,
 pero respetando las siguientes condiciones: un rey nunca puede tener más de 1 (otro) rey en sus casillas adyacentes, 
 y la cantidad total de soldados debe mayor que la cantidad de reyes, pero menor al doble de la cantidad total de reyes
  (ej: si hay 10 reyes, puede haber 15 soldados , pero no 5 soldados, 20 soldados, ni 30 soldados).
"""
from simpleai.search import CspProblem, backtrack
from itertools import combinations


#----------------------------------------- VARIABLES-------------------------------------------------------
variables = []
for row in range(7):
    for col in range(7):
        variables.append((row, col))

#----------------------------------------- DOMINIOS--------------------------------------------------------

for v in variables:
    dominios[v] = ['R','S']
    
#------------------------------------------ RESTRICCIONES---------------------------------------------------
def no_mas_de_un_rey_adyacente(variables,values):
    movimientos = (
        (0,1),
        (0,-1),
        (1,0),
        (-1,0),
    )
    
    for indice, valor in enumerate(values):
        if valor == 'R':
            row, col = variables[indice]
            c = 0
            for mov in movimientos:
                row_2,col_2 = mov
                nueva_pos = (
                    (row + row_2, col + col_2)
                )
                puedo = (
                    0 <= nueva_pos[0] <= 6
                    and 0 <= nueva_pos[1] <= 6
                )
                if puedo:
                    for index, var in enumerate(variables):
                        if var == nueva_pos and values[index] == 'R':
                            c += 1
                    if c>1:
                        return False
                    
    return True                
     
                    