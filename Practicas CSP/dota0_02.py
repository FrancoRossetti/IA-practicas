from simpleai.search import CspProblem, backtrack
from itertools import combinations
"""
En el dota 0.02, el héroe tiene la posibilidad de comprar ítems que mejoran sus habilidades de combate. Pero algunos de esos items son demasiado costosos, 
o tienen consecuencias negativas si se combinan con otros.
Se desea elegir 3 ítems para el héroe, de la siguiente lista de posibles ítems:

-Assault cuirass: armadura que acelera los ataques (costo: 5000).
-Battlefury: hacha que hace mucho daño, daña a enemigos cercanos, y regenera vida (costo: 4000).
-Cloak: capa con resistencia a conjuros (costo: 500).
-Hyperstone: piedra que acelera muchísimo los ataques (costo: 2000).
-Quelling blade: hacha que mejora levemente el daño (costo: 200).
-Shadow blade: espada que acelera los ataques y mejora el daño (costo: 3000).
-Veil of discord: capa que regenera vida y mejora a nivel general al personaje (costo: 2000).

Pero en la elección se deben respetar las siguientes condiciones:

-Se dispone de 6000 monedas de oro para gastar en total, los ítems comprados no pueden superar esa suma.
-Hyperstone no se puede utilizar junto con Shadow blade, porque sus efectos no se suman.
-Quelling blade y Shadow blade no pueden utilizarse juntas, porque sus efectos no se suman.
-Cloak y Veil of discord no pueden utilizarse juntas, porque una es componente de la otra.
-Como mínimo se debe tener 1 ítem que regenere vida.
-Los ítems son únicos, no se puede tener dos veces el mismo ítem.
"""

variables = ['slot_a','slot_b','slot_c']
constraints=[]
regeneran = ['Battlefury','Veil of discord']

costos={'Assault cuirass':5000,'Battlefury':4000,'Cloak':500,'Hyperstone':200,'Quelling blade':200,'Shadow blade':3000,'Veil of discord':2000}

for variable in variables:
    domains[variable] = [
        'Assault cuirass',
        'Battlefury',
        'Cloak',
        'Hyperstone',
        'Quelling blade',
        'Shadow blade',
        'Veil of discord',
    ]

def maximum_cost(variables):
    #variables = ('Assault cuirass','Cloak','Hyperstone')
    cost = 0
    for v in variables:
        valor = costos.get(v)
        cost += valor
    return cost <= 6000

constraints.append(
    (('slot_a','slot_b','slot_c'), maximum_cost)
)

    
def hyperstone_shadowblade(variables):
    #variables = ('Assault cuirass','Cloak')
    item1,item2 = variables
    mala_combinacion = {'Hyperstone','Shadow blade'} # esto es un set
    return set(values) != mala_combinacion

for variable1, variable2 in combinations(variables,2)if __name__ == "__main__":
    restricciones.append((variable1,variable2), hyperstone_shadowblade)


def cloak_veil(variables):
    #variables = ('Assault cuirass','Cloak')
    item1,item2 = variables
    if ('Cloak' in variables and 'Veil of discord' in variables):
        return False
    return True

for item_1, item_2 in combinations(variables, 2):
    constraints.append(
        ((item_1,item_2), cloak_veil)
    )



def quellingblade_shadowblade(variables):
    #variables = ('Assault cuirass','Cloak')
    item1,item2 = variables
    if ('Quelling blade' in variables and 'Shadow blade' in variables):
        return False
    return True

for item_1, item_2 in combinations(variables, 2):
    constraints.append(
        ((item_1,item_2), quellingblade_shadowblade)
    )

def item_regenerehp(variables):    
    #variables = ('Assault cuirass','Cloak','Hyperstone')
    for v in variables:
        if v in regeneran
            return True
    return False

for item_1, item_2,item_3 in combinations(variables, 3):
    constraints.append(
        ((item_1,item_2), item_regenerehp)
    )
    
def mismo_item(variables):
    return len(set(variables)) == 3

for item_1, item_2 in combinations(variables, 3):
    constraints.append(
        ((item_1,item_2), item_regenerehp)
    )
    
print(variables)
print(domain)
result = backtrack(CspProblem(variables,domain,constraints))
print('Result:')
print(result) 
