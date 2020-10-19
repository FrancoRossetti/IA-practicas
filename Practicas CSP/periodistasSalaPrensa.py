from simpleai.search import (
    backtrack,
    min_conflicts, 
    CspProblem
)

from itertools import combinations

#---------------------------------------------VARIABLES-----------------------------------------------------#
variables = ['CNN1','CNN2','FOX','BBC','ONION','MSNBC1','MSNBC2','MSNBC3','RT','INFOBAE1','INFOBAE2']

#---------------------------------------------DOMINIO-----------------------------------------------------#

#EL DICCIONARIO CONTIENE TUPLAS DONDE LA PRIMER POSICION ES LA FILA Y LA SEGUNDA LA COLUMNA
dominios = {}

dominios['CNN1'] = [(0,1),(0,2)]
dominios['CNN2'] = [(0,2),(0,1)]
dominios['FOX'] = [(0,0),(0,3)]
dominios['BBC'] = [(0,3),(0,0)]
dominios['ONION'] = [(2,0),(2,1),(2,2),(2,3)]


lista_no_dominio = ['CNN1','CNN2','FOX','BBC','ONION']
for v in variables:
    if v not in lista_no_dominio:
        lista = []
        for row in range(3):
            for col in range(4):
                lugar = (row,col)
                lista.append(lugar)
        dominios[v]=lista

#---------------------------------------------RESTRICCIONES-----------------------------------------------------#

restricciones =[]

#RESTRICCION DE PERIODISTAS MSNBC
def periodistas_msnbc_contiguos(variables, values):
    per1, per2, per3 = variables
    ub1, ub2, ub3 = values
    if ((ub1[0] == ub2[0]) and (ub1[0]== ub3[0])):
        x = list([ub1[1], ub2[1], ub3[1]])
        if x == [0,1,2] or x == [1,2,3]:
            return True
    return False

restricciones.append(
    (('MSNBC1','MSNBC2','MSNBC3'), periodistas_msnbc_contiguos)
)


def posicion_RT(variables, values):
    pos_rt, pos_cnn1, pos_cnn2 = values
    posicion_adyascente = (
        (0,1),
        (1,0),
        (-1,0),
        (0,-1)
    )

    for pos in posicion_adyascente:
        nueva_pos = (
            pos_rt[0] + pos[0],
            pos_rt[1] + pos[1] 
        )
        if nueva_pos == pos_cnn1 or nueva_pos == pos_cnn2:
            return False
    return True

restricciones.append(
    (('RT','CNN1','CNN2'), posicion_RT)
)


def pos_infobae(variables, values):
    pos_1, pos_2 = values
    if  (abs(pos_1[1]- pos_2[1]) != 1):
        return True
    return False

restricciones.append(
    (('INFOBAE1','INFOBAE2'), pos_infobae)
)

def distintos(variables, values):
    return values[0] != values[1]

for per_1, per_2 in combinations(variables, 2):
    restricciones.append(
        ((per_1, per_2), distintos)
    )

result = min_conflicts(CspProblem(variables, dominios, restricciones))
print('Result: ')
print(result)