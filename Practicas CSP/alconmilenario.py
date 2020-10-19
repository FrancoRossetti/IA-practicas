from simpleai.search import (CspProblem, backtrack, min_conflicts,
                             MOST_CONSTRAINED_VARIABLE,
                             LEAST_CONSTRAINING_VALUE,
                             HIGHEST_DEGREE_VARIABLE)
from itertools import combinations

#---------------------------VARIABLES----------------------------------------#
variables = ('p1','p2','p3','p4','p5','p6','p7','p8')

INTERCONECTADAS = {
    'p1': ['p2', 'p3'],
    'p2': ['p1', 'p3'],
    'p3': ['p2', 'p1'],
    'p4': [],
    'p5': ['p6'],
    'p6': ['p5'],
    'p7': ['p8'],
    'p8': ['p7'],
}

#---------------------------DOMINIOS----------------------------------------#
domains = {}
for var in variables:
    domains[var] = [
        'escudo mejorado',
        'sistema de comunicaciones'
    ]

domains['p7'].extend(['motor de salto a velocidad de la luz','sistema de evasión','sistema de ocultamiento','bahía médica'])
domains['p1'].extend(['lanzador de torpedos de protones','sistema de apuntamiento de armas'])
domains['p2'].extend(['lanzador de torpedos de protones','sistema de apuntamiento de armas'])
domains['p3'].append('sistema de apuntamiento de armas')
domains['p4'].extend(['sistema de apuntamiento de armas','sistema de ocultamiento'])
domains['p8'].extend(['motor de salto a velocidad de la luz','sistema de evasión','sistema de ocultamiento','bahía médica'])
domains['p6'].extend(['bahía de carga mejorada','sistema de ocultamiento','bahía médica'])
domains['p5'].extend(['bahía de carga mejorada','bahía médica'])


    
#---------------------------RESTRICCIONES----------------------------------#

restricciones = []

#ITEM 3
def verificarMotorYOcultamiento(variables, values):
    return not('motor de salto a velocidad de la luz' in values and 'sistema de ocultamiento' in values)

#ITEM 6
def soloUna(variables, values):
    return len(set(values)) == len(values)


#ITEM 10
def EscudoComunicaciones2(variables,values):
    if (('escudo mejorado' in values) and ('sistema de comunicaciones' in values)):
        var1,var2 = variables
        if var1 in INTERCONECTADAS[var2]:
            return False
    return True

def torpedos_apuntamiento(variables,values):
    vars1,vars2 = variables
    if (('lanzador de torpedos de protones' in values) and ('sistema de apuntamiento de armas' in values)):
        var1,var2 = variables
        
        if var2 not in INTERCONECTADAS[var1]:
            return False
        
    return True

for pos1, pos2 in combinations(variables, 2):
    restricciones.append(((pos1,pos2), soloUna))
    restricciones.append(((pos1,pos2), verificarMotorYOcultamiento))
    restricciones.append(((pos1, pos2), torpedos_apuntamiento))
    restricciones.append(((pos1, pos2), EscudoComunicaciones2))




result = min_conflicts(CspProblem(variables, domains, restricciones))
print('Result: ')
print(result)
