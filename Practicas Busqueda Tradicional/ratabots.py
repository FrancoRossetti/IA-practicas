#-----------------------Ejercicio Ratabots--------------------------
# Estado: posición del ratabot (en una tupla). Estado inicial: (3,5)
# Acciones: lista de posibles movimientos del ratabot.


from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    iterative_limited_depth_first,
    uniform_cost,
    astar,
)

from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL_STATE = ((3,5),((1,2),(3,4),(4,0),))

OBSTACULOS = (
    (0,3),
    (0,5),
    (1,1),
    (1,3),
    (2,2),
    (2,4),
    (3,0),
    (4,1),
    (4,3),
    (4,5),
    (5,3),
)

COMIDAS = (
    (1,2),
    (3,4),
    (4,0),
)

PUERTAS = (3,5)

class RatabotsProblem(SearchProblem):

    def cost(self,state1,action,state2):
        return 1
    
    def is_goal(self,state):    
        #la tupla indica la posicion de la rata y la cantidad de comidas que le falta comer.
        return state == ((3,5),())

    def actions(self,state):
        acciones_posibles = []
        ratabot, morfis = state
        movimientos = (
            (-1,0),
            (1,0),
            (0,-1),
            (0,1),
        )

        for movimiento in movimientos:
            fila_ratabot, columna_ratabot = ratabot
            cambio_fila, cambio_columna = movimiento
            nueva_posicion = (
                fila_ratabot + cambio_fila,
                columna_ratabot + cambio_columna,
            )
            puedo = (
                (nueva_posicion not in OBSTACULOS)
                and  (0 <= nueva_posicion[0] <= 5)
                and  (0 <= nueva_posicion[1] <= 5)
            )
            if puedo:         
                acciones_posibles.append((nueva_posicion))

        return acciones_posibles  

    def result(self, state, action):
        nueva_posicion=action
        state = list(state)
        ratabot, morfis = state
        state[0]=nueva_posicion

        if (nueva_posicion in morfis):
            #si la nueva posicion esta en morfis, entonces saca del estado a la comida de esa posicion
            morfis = list(morfis)     
            morfis.pop(morfis.index(nueva_posicion))
            morfis = tuple(morfis)
            
        state[1]=morfis            
        return tuple(state)

    def heuristic(self,state):
        ratabot, morfis = state
        return len(morfis)


metodos = (
    astar,
    #breadth_first,
    #depth_first,
    #iterative_limited_depth_first,
    #uniform_cost,
)

for metodo_busqueda in metodos:
    print()
    print('=' * 50)
    print("corriendo:", metodo_busqueda)
    visor = BaseViewer()
    problem = RatabotsProblem(INITIAL_STATE)
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

