from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    iterative_limited_depth_first,
    uniform_cost,
)
from simpleai.search.traditional import astar

from simpleai.search.viewers import WebViewer, BaseViewer

RACKS = (
    ((0,0),(1,0),(2,0)), #R0
    ((0,2),(1,2),(2,2)), #R1
    ((0,4),(1,4),(2,4)), #R2 
    ((4,0),(5,0),(6,0)), #R3
    ((4,2),(5,2),(6,2)), #R4
    ((4,4),(5,4),(6,4)), #R5
)

POSICION_RACKS = (
    ((0,1),(1,1),(2,1)), #R0
    ((0,3),(1,3),(2,3)), #R1
    ((0,5),(1,5),(2,5)), #R2 
    ((4,1),(5,1),(6,1)), #R3
    ((4,3),(5,3),(6,3)), #R4
    ((4,5),(5,5),(6,5)), #R5
)


#Primer valor: posicion del robot
#Segundo valor: cajas cargadas en el robot
#Tercer valor: cajas no cargadas y restantes por acomodar

INITIAL_STATE = ((3,5),(),((0,3),(6,1),(2,5)))
GOAL_STATE = ((3,5),(),())

class AmagonProblem(SearchProblem):
    def cost(self,state1,action,state2):
        return 1
    
    def actions(self,state):
        robot, cajas_cargadas, cajas_restantes = state
        acciones_disponibles = []
        
        
        #Pregunto primero si esta en la entrada y tiene que cargar
        if (robot == (3,5) and len(cajas_cargadas) < 2): #si esta en la entrada 
            for caja in cajas_restantes:
                acciones_disponibles.append(('CARGAR',caja)) #(('CARGAR',3,4)) != (('CARGAR',2,5))
           
        
        #Por ultimo agrego en las acciones los movimientos que puede hacer
        movimientos = (
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
        )
        
        robot_x,robot_y = robot
        for m in movimientos:
            nueva_posicion = (
                robot_x + m[0],
                robot_y + m[1],
            )    
            puedo = (
                (nueva_posicion not in RACKS)
                and (0 <= nueva_posicion[0] <= 6)
                and (0 <= nueva_posicion[1] <= 5)
            )
            if puedo:
                acciones_disponibles.append(('MOVER',nueva_posicion))
                
        
        return acciones_disponibles

    
    def is_goal(self,state):
        pos_robot, cajas_cargadas, cajas_restantes = state
        return pos_robot == (3,5) and len(cajas_restantes) == 0 and len(cajas_cargadas) == 0
    
    def result(self,state,action):
        state = list(state)
        robot, cajas_cargadas, cajas_restantes = state
        accion, x = action
        if accion == "MOVER":
            state[0] = x          
            for pos in POSICION_RACKS:
                if (state[0] in pos and state[0] in cajas_cargadas): 
                    cajas_cargadas = list(cajas_cargadas)
                    cajas_cargadas.remove(x)
                    state[1] = tuple(cajas_cargadas)
                    break
            state[1] = tuple(cajas_cargadas)
        else:    
            #quiere decir que CARGA una caja
            caja = x
            cajas_cargadas = list(cajas_cargadas)
            cajas_restantes = list(cajas_restantes)
            cajas_cargadas.append(x)
            cajas_cargadas = tuple(cajas_cargadas)
            state[1] = cajas_cargadas
            cajas_restantes.remove(x)
            state[2] = tuple(cajas_restantes)

        return tuple(state)
        


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
    problem = AmagonProblem(INITIAL_STATE)
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