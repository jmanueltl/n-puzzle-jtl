Programa que resuelve el algoritmo de n-puzzle

USEAGE:
--------

Comando:
$ python driver.py [search_method] [puzzle]

metodos usados: 'bfs', 'dfs' or 'ast'
ejemplo de uso:
$ python driver.py ast 0,2,5,6,3,4,1,7,8

Representacion del puzzle.
0 2 5
6 3 4
1 7 8


Implementacion de la solucion
1 2 3
4 5 6
7 8 0  



SALIDA:
----------

path_to_goal
cost_of_path
nodes_expanded
fringe_size
max_fringe_size
search_depth
max_search_depth
running_time
max_ram_usage

or

'solution not possible' (many grids are not solvable eg. 0,1,2,3)




SEARCH METHOD
------------

bfs - breadth-first search  : Busqueda en anchura.
dfs - depth-first search : busqueda en profundidad.
ast - A* search, Algoritmo A* con la heuristica de Manhattan.

