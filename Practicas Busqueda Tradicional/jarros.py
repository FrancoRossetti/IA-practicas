#Se tienen N jarros enumerados de 1 a N, donde la capacidad en litros del jarro I es I. Esto es, el jarro 1 tiene capacidad de 1 litro, 
# el jarro 2, 2 litros y así sucesivamente. Inicialmente el jarro N está lleno de agua y los demás están vacíos.

#El objetivo es que todos los jarros queden con 1 litro de agua, teniendo como operaciones permitidas trasvasar el contenido de un jarro a otro, 
#operación que finaliza al llenarse el jarro de destino o vaciarse el jarro de origen.

#Todo esto se tiene que lograr con el menor costo posible, siendo I el costo de trasvasar el contenido del jarro I a otro jarro.

#En este caso concreto se tienen 4 jarros.


from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    iterative_limited_depth_first,
    uniform_cost,
)

from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL_STATE = (0,0,0,4)  
GOAL_STATE = (1,1,1,1)

#Las acciones serían: (jarra_a_vaciar, jarra_a_llenar)

class JarrosProblem(SearchProblem):
    def cost(self, state1, action, state2):
        costo = action[0] + 1
        return costo
    
    def is_goal(self, state):
        return state == GOAL_STATE

    def actions(self, state):
        acciones_posibles = []
        for jarra_a_vaciar, cantidad_jarra in enumerate(state):  
            if cantidad_jarra > 1: #si la jarra puede vaciarse
                for jarra_a_llenar, cantidad_jarra2 in enumerate(state): 
                    #si son distintas y la jarra a llenar puede recibir al menos un litro
                    if ((jarra_a_vaciar != jarra_a_llenar) and (cantidad_jarra2 < (jarra_a_llenar + 1)): 
                        accion = (jarra_a_vaciar, jarra_a_llenar) 
                        acciones_posibles.append(accion)
        return acciones_posibles

    def result(self, state, action):
        jarra_a_vaciar, jarra_a_llenar = action 
        nuevo_estado = list(state)              
        nuevo_estado[jarra_a_vaciar] -= 1       
        nuevo_estado[jarra_a_llenar] += 1          
        nuevo_estado = tuple(nuevo_estado)
        return nuevo_estado

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
    problem = JarrosProblem(INITIAL_STATE)
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


def heuristic(self, state):
        """
        Asumimos que no importa que los caníbales sean más que los misioneros.
        """
        genteizquierda, , _ = state

        total_gente_pendiente = sum(gente_izquierda)
        idas_necesarias = total_gente_pendiente / 2
        vueltas_necesarias = idas_necesarias - 1
        idas_extras_necesarias = vueltas_necesarias / 2

def heuristic(self, state):
    #asumimos que se pasa de a 1 litro.
    jarra_1, jarra_2=state
    

