from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    iterative_limited_depth_first,
    uniform_cost,
)

from simpleai.search.viewers import WebViewer, BaseViewer
"""
El tour del Caballero
En el problema “Tour del Caballero” se trata de encontrar una secuencia de movimientos de una sola pieza (caballo) en un tablero de ajedrez, 
de modo que se visiten todas las casillas una sola vez. 
El “Caballero” puede comenzar en cualquier posición y 
hay que moverse según las reglas normales para mover un caballo en el juego de ajedrez (en forma de L).

"""
INITIAL_STATE = ((0,0),())  #recorres del 1 al 7 en filas y columnas, y vas viendo si esta en el estado 
print(list(INITIAL_STATE))

class TourCaballeroProblem(SearchProblem):
    
    def cost(self,state1,action,state2):
        return 1
    
    def is_goal(self,state):    
        #la tupla indica la posicion de la rata y la cantidad de comidas que le falta comer.
        lista = list(state[1])
        return len(lista) == 49
        
    def actions(self,state):
        #Movimientos del caballero que puede hacer
        print(state)
        movimientos = (
            (2,1),
            (2,-1),
            (-2,1),
            (-2,1),
            (1,2),
            (1,-2),
            (-1,2),
            (-1,-2),
        )
        acciones_posibles = []
        fila_caballero, columna_caballero = state[0]
        for m in movimientos:
            cambio_fila, cambio_columna = m
            nueva_posicion = (
                fila_caballero + cambio_fila,
                columna_caballero + cambio_columna,
            )
            puedo = (
                (0 <= nueva_posicion[0] <= 7)
                and  (0 <= nueva_posicion[1] <= 7)
                and (nueva_posicion not in state[1])
            )
            if puedo:
                acciones_posibles.append(nueva_posicion)
                
        return acciones_posibles
    
    def result(self, state, action):
        fila_new, columna_new=action
        state = list(state)
        posiciones_recorridas = []
        for s in state[1]:
            posiciones_recorridas.append(s)

        posiciones_recorridas.append(state[0])
        
        state[0] = action
        state[1] = posiciones_recorridas
        state = tuple(state)
        return state
        
        
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
    problem = TourCaballeroProblem(INITIAL_STATE)
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
        print('RECORRIDO: ', RECORRIDO)
