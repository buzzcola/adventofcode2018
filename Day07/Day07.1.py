from Shared import TaskGraph
with open('input','r') as f: input = f.read() 

g = TaskGraph(input)
current_nodes = set(g.getStartTasks())
answer = []

def node_is_ready(node):
    unprocessed_predecessors = set(g.getPredecessors(node)) - set(answer)
    return not any(unprocessed_predecessors)

while any(current_nodes):
    available = filter(node_is_ready, current_nodes)
    next = min(available)
    current_nodes.remove(next)
    answer.append(next)
    unprocessed_successors = set(g.getSuccessors(next)) - set(answer)
    current_nodes.update(unprocessed_successors)

print ''.join(answer)