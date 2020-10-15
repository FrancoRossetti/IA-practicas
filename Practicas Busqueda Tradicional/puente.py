"""
Un grupo de 5 personas quiere cruzar un viejo y estrecho puente. Es una noche cerrada y se necesita llevar una linterna para cruzar. 
El grupo sólo dispone de una linterna, a la que le quedan 5 minutos de batería. Cada persona tarda en cruzar 10, 30, 60, 80 y 120 segundos, respectivamente. 
El puente sólo resiste un máximo de 2 personas cruzando a la vez, y cuando cruzan dos personas juntas caminan a la velocidad del más lento. 
No se puede lanzar la linterna de un extremo a otro del puente, así que cada vez que crucen dos personas, alguien tiene que volver a cruzar hacia atrás con 
la linterna a buscar a los compañeros que faltan, y así hasta que hayan cruzado todos.
"""
from simpleai.search import (
    SearchProblem, 
    breadth_first, 
    depth_first, 
    uniform_cost,
    iterative_limited_depth_first,
    astar
)

import itertools

tiempos = [10,30,60,80,120]

#El estado lo represento como una tupla con -> 
        #tupla[0] = todas las personas y el lado en que se encuentran (0 = izq / 1 = der)
        #tupla[1] = lado en el que se encuentra la linterna
        #tupla[2] = tiempo transcurrido en segundos

INITIAL_STATE = ((0,0,0,0,0),0,0)

from simpleai.search.viewers import WebViewer, BaseViewer

class puenteProblem(SearchProblem):
    def is_goal(self, state):
        personas = (1,1,1,1,1)
        return state[0] == personas and state[2] <= 300

    def actions(self, state):
        #LA ACCION SERIA -> (CANTIDAD A MOVER, INDICE PERSONA1, INDICE PERSONA2)
        
        acciones_disponibles = []
        personas, pos_lintera, tiempo = state

        for indice_persona, posicion_persona in enumerate(personas):
            if (posicion_persona == pos_lintera):
                acciones_disponibles.append((1, indice_persona, 5))
        
        for indice_persona_1, posicion_persona_1 in enumerate(personas):
            for indice_persona_2, posicion_persona_2 in enumerate(personas):
                if ((indice_persona_1 != indice_persona_2) and (posicion_persona_1 == pos_lintera) and (posicion_persona_2 == pos_lintera)):
                    acciones_disponibles.append((2, indice_persona_1, indice_persona_2))
        
        return acciones_disponibles
    
    def result(self, state, action):
        state = list(state)
        
        personas = list(state[0])
        pos_lintera = state[1]
        tiempo_hasta_ahora = state[2]

        cantidad, indice_persona_1, indice_persona_2 = action

        personas[indice_persona_1] =  1 - personas[indice_persona_1]

        tiempo = tiempos[indice_persona_1]        
        if (cantidad == 2):
            personas[indice_persona_2] =  1 - personas[indice_persona_2]
            if (tiempos[indice_persona_2] > tiempos[indice_persona_1]):
                tiempo = tiempos[indice_persona_2]

        pos_lintera =  1 - pos_lintera
        tiempo_hasta_ahora += tiempo

        personas = tuple(personas)
        state = (personas, pos_lintera, tiempo_hasta_ahora)
        return tuple(state)

    def cost(self, state_ini, action, state_fin):
        cantidad, indice_persona_1, indice_persona_2 = action
        if (cantidad == 1):
            return tiempos[indice_persona_1]
        else:
            if (tiempos[indice_persona_1 > tiempos[indice_persona_2]]):
                return tiempos[indice_persona_1]
            else:
                return tiempos[indice_persona_2]

metodos = (
    #astar,
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
    problem = puenteProblem(INITIAL_STATE)
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
