"""
Una nave alienígena se ha estrellado en la Tierra, y un grupo de investigadores desea abrir su escotilla principal. Pero la misma posee un mecanismo bastante extraño, que consta de una serie de botones que deben ser presionados en orden para lograr una combinación de números en una pantalla.
La pantalla posee 3 casillas alineadas una al lado de la otra, cada una con un número dentro. Inicialmente todas poseen el número cero. Los botones que pueden presionarse son los siguientes:
-Botón rojo: Suma 3 al casillero inicial.
-Botón verde: Resta 2 al casillero inicial.
-Botón amarillo: Intercambia los valores de las dos primeras casillas.
-Botón celeste: Intercambia los valores de las dos últimas casillas.
La secuencia de números que se debe lograr para abrir la escotilla es la siguiente:  5, 1, 8
a) Plantee formalmente como problema de búsqueda tradicional, con código y comentarios explicativos.
b) Plantee una heurística para el mismo. No hace falta que sea muy precisa, pero debe ser admisible.
"""

from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    iterative_limited_depth_first,
    uniform_cost,
)
from simpleai.search.traditional import astar

from simpleai.search.viewers import WebViewer, BaseViewer

BOTONES = ("Rojo","Verde","Amarillo","Celeste")

CASILLERO_INICIAL = 0
INITIAL_STATE = (0,0,0)
GOAL_STATE = (5,1,8)

class AlienigenaProblem(SearchProblem):
    def actions(self, state):
        #las acciones son todos los botones.
        acciones_posibles=[]
        for b in BOTONES:
            acciones_posibles.append(b)
        return acciones_posibles
        
    def cost(self,state1,action,state2):
        return 1
    
    def is_goal(self,state): 
        return state == GOAL_STATE
    
    def result(self, state, action):
        state = list(state)
        if action == "Rojo":
            state[CASILLERO_INICIAL] += 3
        if action == "Verde":
            state[CASILLERO_INICIAL] -= 2
        if action=="Amarillo":
            aux = state[0]
            state[0]=state[1]
            state[1]=aux
        if action=="Celeste":
            aux = state[1]
            state[1]=state[2]
            state[2]=aux
        return tuple(state)
    
    def heuristic(self, state):
        """
            Asumimos que solo importan dos, el 3ero no importa
        """
        state = list(state)
        contador = 0
        for index, casilla in enumerate(state):
            if (casilla == GOAL_STATE[index]):
                contador += 1
                if (index == 1):
                    break
        return contador
    
metodos = (
    #breadth_first,
    #depth_first,
    #iterative_limited_depth_first,
    #uniform_cost,
    astar,
)

for metodo_busqueda in metodos:
    print()
    print('=' * 50)
    print("corriendo:", metodo_busqueda)
    visor = BaseViewer()
    problem = AlienigenaProblem(INITIAL_STATE)
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