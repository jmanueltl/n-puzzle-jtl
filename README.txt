n-puzzle solver
Andy Davies
____________________________

A Python program that solves any given n-puzzle.

See https://en.wikipedia.org/wiki/15_puzzle


USEAGE:
--------

In the command line:
$ python driver.py [search_method] [puzzle]

where search_method: 'bfs', 'dfs' or 'ast'
where puzzle is a comma-seperated list of numbers from 0 to n^2-1

eg.
$ python driver.py ast 0,2,5,6,3,4,1,7,8

represents the puzzle
0 2 5
6 3 4
1 7 8
where 0 is the blank space

This implementation treats the goal state as:
1 2 3
4 5 6
7 8 0   (some have the zero at top left)



RETURNS:
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

bfs - breadth-first search
dfs - depth-first search
ast - A* search, in this case using the total Manhattan Distance heuristic

Note: the point of this project was to see the different time and memory useage for each search_method. As such don't be surprised if bfs or dfs takes a very long time. Use A* search for best results.

At a search depth of just 10 (10 moves to solution), bfs takes 3 hours and 10 terabytes of memory!
  


WHY?
-----

1. To learn Python. This is the first thing I've ever made using Python.

2. To start to learn about Artificial Intelligence, in particular the time and space complexities of search algorithms.


