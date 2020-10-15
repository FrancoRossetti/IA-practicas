from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    iterative_limited_depth_first,
    uniform_cost,
)

from simpleai.search.viewers import WebViewer, BaseViewer




INITIAL_STATE = ((2,0),((1,1),(0,2)))  # state[0]: posicion del heroe, state[1]: posicion de los enemigos



class Dota2Problem(SearchProblem):

    
    def cost(self,state1,action,state2):
        return 1
    # heuristica: asumiendo que ataco y m  quedo en el lugar del enemigo
    def is_goal(self,state):    
        # Cuando elimino a la base o al heroe enemigo, lo saco de la tupla. 
        # entonces, si state[1] no tiene datos, entonces retorno true. (no se como ponerlo)
        return state[1] == None

    def actions(self,state):
        acciones_posibles = []
        heroe, enemigos = state
        movimientos = (         #lista de movimientos que puedo hacer
            (-1,0),
            (1,0),
            (0,-1),
            (0,1),
        )
        for movimiento in movimientos:          
            enemigos = state[1]  #saco los enemigos
            fila_heroe, columna_heroe = heroe    #saco la fila y columna del heroe
            cambio_fila, cambio_columna = movimiento #saco la fila y columna de la posicion
            nueva_posicion = (fila_heroe + cambio_fila, columna_heroe + cambio_columna,)          

            puedo = (                 #no se debe pasar del mapa
                     (0 <= nueva_posicion[0] <= 2)
                and  (0 <= nueva_posicion[1] <= 2)
            )                           
            
            if puedo:           
                if (nueva_posicion in enemigos):
                    #si la nueva posicion esta en enemigos, entonces saco del estado a los enemigos de esa posicion 
                    enemigos = list(enemigos)     
                    enemigos.pop(enemigos.index(nueva_posicion))
                    enemigos = tuple(enemigos)                        
                acciones_posibles.append((nueva_posicion,enemigos)) #((2,0),((1,1))

    def result(self, state, action):  
        #aca convierto en lista, y meto la nueva posicion del heroe y los enemigos restantes.
        nueva_posicion,enemigos=action
        state = list(state)
        state[0]=nueva_posicion        
        if (nueva_posicion in enemigos):
            #si la nueva posicion esta en enemigos, entonces saco del estado a los enemigos de esa posicion 
            enemigos = list(enemigos)     
            enemigos.pop(enemigos.index(nueva_posicion))
            enemigos = tuple(enemigos)                        

        state[1]=enemigos

        return tuple(state)