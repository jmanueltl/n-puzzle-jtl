class Metric:

    def __init__(self):

        self.path_to_goal = []

        self.nodes_expanded = 0

    def cost_of_path(self):
        return len(self.path_to_goal)