import sys 
import grid

# validate command line input
if len(sys.argv) != 3:
	sys.stderr.write('Error: must be 3 command line arguments of the form:\npython driver.py <method> <board>\n')
	sys.exit()

if sys.argv[1] not in ['bfs', 'dfs', 'ast', 'ida']: 
	sys.stderr.write('<method> argument must be one of bfs, dfs, ast, ida\n')
	sys.exit()

input_state = sys.argv[2].split(',')

# TODO: check that input grid is perfect square and contains all integers 0 to (len(input_state) - 1)


# instantiate state object
grid = grid.Grid(input_state)
# test
print(grid.state)

# test
grid.move_left()

print 'after moving to left'
print(grid.state)