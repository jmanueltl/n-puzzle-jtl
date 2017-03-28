import grid
import custom_structures
import copy
import math
import metric

class Solver:
    """ Controller. Takes an input list, returns path solution """
    
    def __init__(self, input_list):
        
        # not all grids are solvable
        if not self.solvable(input_list):
            raise ValueError('A solution is not possible')

        # don't just bind to input state. we want the object to have its OWN state
        # https://docs.python.org/2/library/copy.html
        self.initial_state = copy.deepcopy(self.list_to_grid(input_list)) 
        
        # set goal state
        # TODO: this smells wrong. Is it?
        self.goal_state = self.set_goal_state(input_list)

        # using custom structure so we can implement a custom __contains__
        self.frontier = custom_structures.Frontier()        
        self.explored = custom_structures.Explored()

        self.metrics = metric.Metric(self.frontier)




    def uninformed_search(self, search_method):

        self.metrics.start_timer()

        initial_grid = grid.Grid(self.initial_state)

        # add initial to the frontier
        self.frontier.queue.append(initial_grid)
        
        # while queue is not empty..
        while self.frontier.queue:
            # TODO: better name for state. It's a grid. state.state is the state!
            
            if search_method == 'bfs':
                state = self.frontier.queue.popleft() 
            elif search_method == 'dfs': 
                state = self.frontier.queue.pop()  
            
            # update depth metrics
            self.metrics.search_depth = len(state.path_history)
            self.metrics.update_max_depth()

            self.explored.set.add(state)

            if self.goal_test(state):
                self.metrics.path_to_goal = state.path_history
                self.metrics.stop_timer()
                self.metrics.measure_ram_useage()                 
                return self.metrics

            # add neighbours of this state to the frontier, if not already in the
            # frontier or explored
            self.expand_nodes(state)

        # if we get to here it's gone tits up
        raise ValueError('Shouldn\'t have got to here - gone tits')

    
    

    
    def expand_nodes(self, starting_grid):
        """ adds all possible next nodes from a state to a frontier set """

        # TODO: should be pushed in reverse order for DFS

        for node in ['up', 'down', 'left', 'right']:   

            # need to create new grid object for each node
            # the program is imagining the future!! (maybe change this name...)
            imagined_grid = grid.Grid(starting_grid.state)

            # pass path history from previous grid to the next grid
            # https://docs.python.org/2/library/copy.html
            imagined_grid.path_history = copy.copy(starting_grid.path_history)

            if imagined_grid.move(node):  # returns false if move not possible
                
                # update path history
                imagined_grid.path_history.append(node)

                # is this new grid already in frontier or explored?
                if imagined_grid not in self.frontier and imagined_grid not in self.explored:
                    self.frontier.queue.append(imagined_grid)

                    self.metrics.update_max_fringe()

        self.metrics.nodes_expanded += 1

                

    def goal_test(self, state):
        
        # TODO: confusing names. state here is not a Grid.state but a Grid

        # ridiculous naming here
        # TODO: is this using strict object comparison here?
        if state.state == self.goal_state:
            return True
        else:
            return False

        
    
    def set_goal_state(self, input_list):

        # initialise empty grid state
        n = int(math.sqrt(len(input_list)))
        goal_state = [['-' for x in range(n)] for y in range(n)]

        # populate goal grid with ordered tiles
        i = 0
        j = 0
        count = 1
        
        while i < n:
            
            if count == n * n:
                count = 0

            goal_state[i][j] = count
            count += 1            

            j += 1
            if j == n:
                j = 0
                i += 1

        return goal_state



    def solvable(self, input_list):

        # turns out a lot of grids are unsolvable.
        # http://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable/838818
        # http://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html

        # solvability depends on the width...
        width = int(math.sqrt(len(input_list)))

        # ...if the row that zero is on id odd/even (can use existing method on Grid for now)
        temp_grid = grid.Grid(self.list_to_grid(input_list)) # TODO: sort this list/grid confusion
        zero_location = temp_grid.locate_zero()
        if zero_location[0] % 2 == 0: y_is_even = True
        else: y_is_even = False

        # .. and the number of 'inversions'

        # strip the blank tile
        input_list = [number for number in input_list if number != 0]

        inversion_count = 0
        list_length = len(input_list)

        for index, value in enumerate(input_list):
            for value_to_compare in input_list[index + 1 : list_length]:
                if value > value_to_compare:
                    inversion_count += 1
                    
        
        if inversion_count % 2 == 0: inversions_even = True
        else: inversions_even = False

        if width % 2 == 0: width_even = True
        else: width_even = False

        # our zero_location tuple counts rows from the top, but we need from the bottom
        if width_even:
            zero_odd = not y_is_even
        # if width not even, we don't need zero_odd
        
        # see the bham.ac.uk link
        return ((not width_even and inversions_even)
               or
               (width_even and (zero_odd == inversions_even)))

        

        
    def list_to_grid(self, tile_list):

        # TODO: this is getting confusing - shouldn't this be a method of grid instead?

        n = int(math.sqrt(len(tile_list)))

        # initialise empty grid
        input_grid = [['-' for x in range(n)] for y in range(n)]

        # populate grid with tiles
        i = 0
        j = 0
        for tile in tile_list:
            input_grid[i][j] = tile
            j += 1
            if j == n:
                j = 0
                i += 1

        return input_grid






        

        




