from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    iterative_limited_depth_first,
    uniform_cost,
)

from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL_STATE = (3,3) #posicion donde arranca el rey

SOLDADOS = (
    (0,0),
    (0,1),
    (0,4),
    (1,4),
    (2,0),
    (3,1),
    (3,6),
    (4,0),
    (6,3),
    (6,5),
    )


class HnefaioerfdProblem(SearchProblem):
    
    def cost(self,state1,action,state2):
        return 1
    
    def is_goal(self,state):
        pos_x, pos_y = state
        band = False
        if ((pos_x == 0) or (pos_x == 6)):
            band = True
        else: 
            if ((pos_y == 0) or (pos_y == 6)):
                band = True                
        return band
    
    def actions(self,state):
        acciones_posibles=[]
        pos_x, pos_y = state
        movimientos = (
            (-1,0),
            (1,0),
            (0,-1),
            (0,1),
        )
        for movimiento in movimientos:
            cambio_x, cambio_y = movimiento
            nueva_posicion = (
                pos_x + cambio_x,
                pos_y + cambio_y,
            )
            puedo = (
                (nueva_posicion not in SOLDADOS)
                and  (0 <= nueva_posicion[0] <= 6)
                and  (0 <= nueva_posicion[1] <= 6)
            )
            if puedo:
                for m in movimientos:
                    camb_x, camb_y = m
                    nueva_pos = (
                        camb_x + nueva_posicion[0],
                        camb_y + nueva_posicion[1],
                    )
                    if nueva_pos in SOLDADOS:
                        puedo=False
                        break
            if puedo:
                acciones_posibles.append(nueva_posicion)                
        return acciones_posibles    
            
    
    def result(self, state, action):
        cambio_x,cambio_y = action
        state = list(state)
        state[0] = cambio_x
        state[1] = cambio_y
        return tuple(state)
    
    
    
metodos = (
    #breadth_first,
    #depth_first,
    #iterative_limited_depth_first,
    uniform_cost,
)    
        
for metodo_busqueda in metodos:
    print()
    print('=' * 50)
    print("corriendo:", metodo_busqueda)
    visor = BaseViewer()
    problem = HnefaioerfdProblem(INITIAL_STATE)
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
