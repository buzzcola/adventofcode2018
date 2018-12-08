from Shared import TaskGraph
with open('input','r') as f: input = f.read() 

g = TaskGraph(input)
current_nodes = set(g.getStartTasks())
task_start_times = {}
time = -1
workers = [None for _ in range(5)]
answer = []

def node_is_ready(node):
    unprocessed_predecessors = set(g.getPredecessors(node)) - set(answer)
    return not any(unprocessed_predecessors)

def task_time_remaining(task):
    duration = 60 + (ord(task) - 64) # ord('A') == 65
    if task in task_start_times:
        age = time - task_start_times[task]
    else:
        age = 0
    return max(duration - age, 0)

while len(answer) < len(g.tasks):
    time += 1
    for i in range(len(workers)):
        if workers[i] and task_time_remaining(workers[i]) == 0:
            answer.append(workers[i])            
            unprocessed_successors = set(g.getSuccessors(workers[i])) - set(answer)
            current_nodes.update(unprocessed_successors)
            workers[i] = None
        
        if not workers[i]:
            available = filter(node_is_ready, current_nodes)
            if any(available):
                workers[i] = min(available)
                current_nodes.remove(workers[i])
                task_start_times[workers[i]] = time

print time