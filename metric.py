class Metric:

    def __init__(self, frontier):

        self.path_to_goal = []

        self.nodes_expanded = 0

        self.fringe = frontier

        self.max_fringe_size = 0

    def cost_of_path(self):
        return len(self.path_to_goal)

    def fringe_size(self):
        return len(self.fringe.queue)

    def set_max_fringe(self):
        fringe_length = self.fringe_size()
        if fringe_length > self.max_fringe_size:
            self.max_fringe_size = fringe_length