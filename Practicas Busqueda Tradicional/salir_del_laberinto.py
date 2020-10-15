from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    iterative_limited_depth_first,
    uniform_cost,
)




from simpleai.search.viewers import WebViewer, BaseViewer


HABITACIONES = {"1": ["9","12"],
    "2":["5","6","7","3"],
    "3":["2","8","4"],
    "4":["5","8","21"],
    "5":["6","2"],
    "6":["5","2","9"],
    "7":["2","9"],
    "8":["3","10","4"],
    "9":["12","6","7","1"],
    "10":["8","11","15"],
    "11":["10"],
    "12":["14","17","9","1"],
    "13":["14","17","19"],
    "14":["13","12"],
    "15":["18","10"],
    "16":["15","20"],
    "17":["13","19","12"],
    "18":["15"],
    "19":["17","13","20"],
    "20":["19","16"]
}

INITIAL_STATE = "1"

class LaberintoProblem(SearchProblem):
    def cost(self,state1,action,state2):
        return 1
    
    def is_goal(self,state):
        return state == "21"
    
    def actions(self,state):
        return HABITACIONES[state]
    
    def result(self, state, action):
        return action
        

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
    problem = LaberintoProblem(INITIAL_STATE)
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
