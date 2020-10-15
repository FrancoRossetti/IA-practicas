from itertools import combinations
from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    iterative_limited_depth_first,
    uniform_cost,
)


INITIAL_STATE2 = [('CA','CA','CO','CO','CE','CE'),(),()]


def actions2(state):
    acciones = []
    for origen in (0,1):
        #movimientos de a 1
        for presidente in set(state[origen]):
            acciones.append(((presidente,), origen))
        
        #movimientos de a 2
        for presi1, presi2 in combinations(state[origen]):
            acciones.append(((presi1,presi2),origen))
            
    #filtrar las acciones (por ejemplo, que un comunista no quede en la sala 1 y el otro en la 3)
    acciones_legales = []
    
    for accion in acciones:
        ilegal=False
        estado_resultado = result(state, accion)
        
        for sala in estado_resultado:
            if len(sala) == 2 and sala[0]==sala[1]:
                ilegal=True
                
        for presidente_en_inicio in estado_resultado[0]:
            if presidente_en_inicio in estado_resultado[2]:
                ilegal = True
                
        if not legal:
            acciones_legales.append(accion)
            