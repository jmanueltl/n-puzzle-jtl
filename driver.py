import sys 
import grid
import solver

# validate command line input
if len(sys.argv) != 3:
	sys.stderr.write('Error: must be 3 command line arguments of the form:\npython driver.py <method> <board>\n')
	sys.exit()

if sys.argv[1] not in ['bfs', 'dfs', 'ast', 'ida']: 
	sys.stderr.write('<method> argument must be one of bfs, dfs, ast, ida\n')
	sys.exit()

search_method = sys.argv[1]

# convert inut string to a list of ints
input_list = sys.argv[2].split(',')
input_list = map(int, input_list)

# TODO: check that input list represents perfect square and contains all integers 0 to (len(input_state) - 1)


# TODO: do we want to pass the input_grid to the solver, or just instantiate 
# a generic Solver and pass inut_grid to the search method?
try:
    solver = solver.Solver(input_list)
except ValueError:
    print 'no solution exists'
    sys.exit()


solution_metrics = solver.uninformed_search(search_method) 




print "path_to_goal: " + str(solution_metrics.path_to_goal)
print "cost_of_path: " + str(solution_metrics.cost_of_path())
print "nodes_expanded: " + str(solution_metrics.nodes_expanded)
print "fringe_size: " + str(solution_metrics.fringe_size())
       