import grid
import Queue
import custom_structures


class Solver:
    """ Controller. Takes a grid state, returns path solution """
    
    def __init__(self, input_grid, n):
        
        self.initial_state = input_grid 
        
        # using custom structure so we can implement a custom __contains__
        self.frontier = custom_structures.Frontier()        
        self.explored = custom_structures.Explored() 

        # set goal state
        # TODO: this smells wrong. Is it?
        self.goal_state = self.set_goal_state(n)




    def breadth_first_search(self):

        initial_grid = grid.Grid(self.initial_state)

        self.expand_nodes(initial_grid)    

        while not self.frontier.queue.empty():
            state = self.frontier.queue.get()    # TODO: this is mental. need another way
            self.explored.set.add(state)

            if self.goal_test(state):
                return state.path_history

            # add neighbours of this state to the frontier, if not already in the
            # frontier or explored
            self.expand_nodes(state)

        # if we get to here it's gone tits up
        raise ValueError('Shouldn\'t have got to here - gone tits')


    
    def expand_nodes(self, starting_grid):
        """ adds all possible next nodes from a state to a frontier set """

        for node in ['up', 'down', 'left', 'right']:   

            # need to create new grid object for each node
            # the program is imagining the future!! (maybe change this name...)
            imagined_grid = grid.Grid(starting_grid.state)

            # pass path history from previous grid to the next grid
            imagined_grid.path_history = starting_grid.path_history

            if imagined_grid.move(node):  # returns false if move not possible
                
                # update path history
                imagined_grid.path_history.append(node)

                # is this new grid already in frontier or explored?
                if imagined_grid not in self.frontier or self.explored:
                    self.frontier.queue.put(imagined_grid)

                

        


    def goal_test(self, state):
        
        # TODO: confusing names. state here is not a Grid.state but a Grid

        # ridiculous naming here
        # TODO: is this using strict object comparison here?
        if state.state == self.goal_state:
            return True
        else:
            return False

        
    
    def set_goal_state(self, n):

        # initialise empty grid state
        goal_state = [['-' for x in range(n)] for y in range(n)]

        # populate goal grid with ordered tiles
        i = 0
        j = 0
        count = 0
        
        while i < n:
            goal_state[i][j] = count
            count += 1
            j += 1
            if j == n:
                j = 0
                i += 1

        return goal_state





        

        




