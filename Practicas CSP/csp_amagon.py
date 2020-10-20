from itertools import combinations

from simpleai.search import (CspProblem, backtrack, min_conflicts,
                             MOST_CONSTRAINED_VARIABLE,
                             LEAST_CONSTRAINING_VALUE,
                             HIGHEST_DEGREE_VARIABLE)

#---------------------------------VARIABLES--------------------------------------#

variables=(('Explosivo',200),
           ('Comida',155),
           ('Toxico',200),
           ('Explosivo',444),
           ('Toxico',25),
           ('Explosivo',210),
           ('Comida',175),
           ('Toxico',100),
           ('Explosivo',454),
           ('Toxico',205),
           ('Explosivo',127),
           ('Toxico',125),)
#---------------------------------DOMINIO----------------------------------------#

domain = {}

racks = ['R0','R1','R2','R3','R4','R5']
for v in variables:
    if v[0] == "Explosivo":
        domain[v] = ['R0','R1']
    else:
        domain[v] = racks
        

#---------------------------------RESTRICCIONES----------------------------------#
constraints = []
def comida_y_toxico(variables,values):
    var1 , var2 = variables
    if (values[0] == values[1]):
        if (var1[0] == 'Toxico' and var2[0] == 'Comida') or (var2[0] == 'Toxico' and var1[0] == 'Comida'):
            return False
    return True
        
for caja1,caja2 in combinations(variables,2):
    constraints.append(
        ((caja1,caja2), comida_y_toxico)
    )

def apilar_10(variables,values):
    for val in values:
        cantidad_rack = 0
        for rack in racks:
            if rack == val:
                cantidad_rack = cantidad_rack + 1
        if cantidad_rack >= 10:
            return False
 
    return True

def suma_kg(variables,values):
    
    for ind_val,val in enumerate(values):
        cantidad_kg_rack = 0
        for rack in racks:
            if rack == val:
                cantidad_kg_rack += variables[ind_val][1] 
        if cantidad_kg_rack >= 1000:
            return False
            
    return True





constraints.append(
    ((variables), apilar_10)
)
constraints.append(
    ((variables),suma_kg)
)

problema = CspProblem(variables, domain, constraints)
resultado = min_conflicts(problema)
print(resultado)
