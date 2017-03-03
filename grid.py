import math

class Grid:
    """ Represents the state of the grid """

    def __init__(self, input_state):
        """ Constructs n x n grid of numbered tiles. input_state is an array of integers """

        n = int(math.sqrt(len(input_state)))

        # initialise empty grid
        self.state = [['-' for x in range(n)] for y in range(n)]

        # populate grid with tiles
        i = 0
        j = 0
        for tile in input_state:
            self.state[i][j] = tile
            j += 1
            if j == n:
                j = 0
                i += 1


    def move_left(self):

        # TODO: seperate model and controller here?
        # TODO: change this to generic move('direction')
        
        # find coordinates of '0' tile
        zero_coords =  [ (index, row.index('0')) for index, row 
                        in enumerate(self.state) 
                        if '0' in row ]

        # swap 0 tile with tile to the RIGHT
        # (when we say 'move left' we mean the tile, not the space (0))   
        tile_to_move = self.state[zero_coords[0][0]][zero_coords[0][1] + 1]
        self.state[zero_coords[0][0]][zero_coords[0][1]] = tile_to_move
        self.state[zero_coords[0][0]][zero_coords[0][1] + 1] = '0'


        # TODO: handle case where cannot move left due to edge of board




        

	
