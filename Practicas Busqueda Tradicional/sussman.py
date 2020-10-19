from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    iterative_limited_depth_first,
    uniform_cost,
)


from simpleai.search.viewers import WebViewer, BaseViewer


metodos = (
    #astar,
    breadth_first,
    #depth_first,
    #iterative_limited_depth_first,
    #uniform_cost,
)


INITIAL_STATE = ('B','AC','')
ESTADO_FINAL = ('','','CBA')

class SussmanProblem(SearchProblem):
    def cost(self,state1,action,state2):
        return 1
    
    def is_goal(self,state):
        return state == ESTADO_FINAL
    
    def actions(self,state):
        acciones = []
        for pos_ini, bloq_ini in enumerate(state):
            if (len(bloq_ini)>0):
                for pos_fin, bloq_fin in enumerate(state):
                    if (pos_fin != pos_ini):
                        acciones.append((pos_ini,pos_fin))                        
        return acciones

    def result(self,state,action):
        state = list(state)
        bloque_inicio = state[action[0]]
        bloque_fin = state[action[1]]
        letra = bloque_inicio[-1]
        bloque_inicio = bloque_inicio[:-1]
        bloque_fin = bloque_fin + letra
        state[action[0]]=bloque_inicio
        state[action[1]]=bloque_fin
        return tuple(state)

for metodo_busqueda in metodos:
    print()
    print('=' * 50)
    print("corriendo:", metodo_busqueda)
    visor = BaseViewer()
    problem = SussmanProblem(INITIAL_STATE)
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

