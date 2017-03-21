import sys 
import grid
import solver
import math

# validate command line input
if len(sys.argv) != 3:
	sys.stderr.write('Error: must be 3 command line arguments of the form:\npython driver.py <method> <board>\n')
	sys.exit()

if sys.argv[1] not in ['bfs', 'dfs', 'ast', 'ida']: 
	sys.stderr.write('<method> argument must be one of bfs, dfs, ast, ida\n')
	sys.exit()

input_list = sys.argv[2].split(',')

# TODO: check that input list represents perfect square and contains all integers 0 to (len(input_state) - 1)

# convert input list into nxn grid

n = int(math.sqrt(len(input_list)))

# initialise empty grid
input_grid = [['-' for x in range(len(input_list))] for y in range(len(input_list))]

# populate grid with tiles
i = 0
j = 0
for tile in input_list:
    input_grid[i][j] = tile
    j += 1
    if j == n:
        j = 0
        i += 1


# testing
# TODO: do we want to pass the input_grid to the solver, or just instantiate 
# a generic Solver and pass inut_grid to the search method?
solver = solver.Solver(input_grid, n)
solution = solver.breadth_first_search() 
print solution







