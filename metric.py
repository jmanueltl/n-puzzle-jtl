class Metric:

    def __init__(self):

        self.path_to_goal = []

        self.nodes_expanded = 0

        self.frontier_at_goal = []

    def cost_of_path(self):
        return len(self.path_to_goal)

    def fringe_size(self):
        return len(self.frontier_at_goal)