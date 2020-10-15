from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    iterative_limited_depth_first,
    uniform_cost,
)
from simpleai.search.traditional import astar

from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL_STATE = ((0,0),(()))

class CaballoPinturaProblem(SearchProblem):
    def cost(self,state1,action,state2):
        return 1
    
    def is_goal(self,state):
        caballo, pinturas = state
        pinturas = list(pinturas)
        return len(pinturas) == 11
    
    def actions(self,state):
        caballo, pinturas = state
        acciones_posibles = []
        movimientos = (
            (2,1),
            (2,-1),
            (-2,1),
            (-2,-1),
            (1,2),
            (1,-2),
            (-1,2),
            (-1,-2),
        )
        for movimiento in movimientos:
            caballo_x, caballo_y = caballo
            nueva_posicion = (
                caballo_x + movimiento[0],
                caballo_y + movimiento[1],
            )
            puedo = (
                (0 <= nueva_posicion[0] <= 2)
                and (0 <= nueva_posicion[1] <= 3)
                and (nueva_posicion not in pinturas)
            )
            if puedo:
                acciones_posibles.append(nueva_posicion)
                
        return acciones_posibles       
    
    def result(self, state, action):
        caballo, pinturas = state
        pinturas = list(pinturas)
        pinturas.append(caballo)
        pinturas = tuple(pinturas)        
        caballo = action
        caballo = tuple(caballo)
        state = (caballo,pinturas)
        return state
    
    
metodos = (
    breadth_first,
    #depth_first,
    #iterative_limited_depth_first,
    #uniform_cost,
)

for metodo_busqueda in metodos:
    print()
    print('=' * 50)
    print("corriendo:", metodo_busqueda)
    visor = BaseViewer()
    problem = CaballoPinturaProblem(INITIAL_STATE)
    result = metodo_busqueda(problem, graph_search = True, viewer = visor)
    print ('estado final:')
    print(result.state)

    print('-' * 50)

    print('estadísticas:')
    print('cantidad de acciones hasta la meta:', len(result.path()))
    print(visor.stats)

    for action,state in result.path():
        print('accion:', action)
        print('estado resultante:', state)