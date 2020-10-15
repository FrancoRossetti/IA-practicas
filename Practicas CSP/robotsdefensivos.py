from simpleai.search import CspProblem, backtrack
from itertools import combinations

"""Luego del último ataque, se decidió incrementar el número de robots a 6, y ya no permanecerán almacenados, 
    sino que se ubicarán en posiciones defensivas fijas y permanentes. Pero deben respetarse algunas restricciones:

- No puede haber dos robots en la misma habitación, generarían demasiadas molestias para los científicos.
- No puede haber dos robots en habitaciones adyacentes, impedirían demasiado la circulación.
- Las habitaciones restringidas siguen sin poder contener robots.
- Las dos habitaciones que poseen puertas al exterior deben contener un robot.
"""

variables = ['1','2','3','4','5','6']

obstaculos = (
    (0,2),(1,3),(2,1),
)

doors = (
    (0,4),
    (3,2),
)

#Agregamos al dominio toda la matriz que es 4x5.
domains = {}
for v in variables:
    lista = []
    for row in range(4):
        for col in range(5):
            lugar = (row,col)
            lista.append(lugar)
    domains[v]=lista
    
constraints=[]


#los robots no deben estar adyacentes
def locations_not_near(variables,values):
    #variables = ('1','2')
    #values = ((1,2),(0,3))
    value_1, value_2 = values
    row_2, col_2 = value_2
    
    near = (
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    )
    
    for n in near:
        row_n, col_n = n
        loc = (
            (row_2 + row_n , col_n + col_2)
        )
        if (value_1 == loc):
            return False

    return True

for robot_x1, robot_x2 in combinations(variables, 2):
    constraints.append(
        ((robot_x1, robot_x2), locations_not_near)
    )

def different_locations(variables,values):
    #variables = ('1','2')
    #values = ((1,2),(0,3))
    value_1, value_2 = values
    return value_1 != value_2

for robot_x1, robot_x2 in combinations(variables, 2):
    constraints.append(
        ((robot_x1, robot_x2), different_locations)
    )
        
def not_in_obstacles(variables, values):
    return values[0] not in obstaculos

        
for robot in variables:
    constraints.append(
        ((robot),not_in_obstacles)
    )

#
def in_doors(variables,values):
    #values = ((1,2),(0,3)) -> todas las posiciones
    c=0
    for v in values:
        if v in doors:
            c+=1
    return c == 2

# vemos si en la combinacion de todos los robots están en las puertas
for robot_x1,robot_x2,robot_x3,robot_x4,robot_x5,robot_x6 in combinations(variables, 6):
    constraints.append(
        ((robot_x1, robot_x2, robot_x3, robot_x4, robot_x5, robot_x6), in_doors)
    )

print(variables)
print(domains)
result = backtrack(CspProblem(variables,domains,constraints))
print('Result:')
print(result) 
