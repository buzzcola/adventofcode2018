class TaskGraph:
    def __init__(self, input):
        self.tasks = set()
        self.edges = []

        for line in input.split('\n'):
            (task1, task2) = (line[5:6], line[36:37])
            self.tasks.update([task1, task2])
            self.edges.append((task1, task2))

    def getPredecessors(self, task):
        return [edge[0] for edge in self.edges if edge[1] == task]

    def getSuccessors(self, task):
        return [edge[1] for edge in self.edges if edge[0] == task]
   
    def getStartTasks(self):
        return [x for x in self.tasks if not any(self.getPredecessors(x))]