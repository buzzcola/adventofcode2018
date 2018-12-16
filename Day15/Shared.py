from __future__ import print_function
from anytree import AnyNode, RenderTree

class Fighter(object):
    def __init__(self):
        self.hitpoints = 200
        self.attack_power = 3
        self.enemy = ''

class Elf(Fighter):
    def __init__(self):
        Fighter.__init__(self)
        self.enemy = 'G'
    
    def __str__(self): return 'E'
   
class Goblin(Fighter):
    def __init__(self):
        Fighter.__init__(self)
        self.enemy = 'E'

    def __str__(self): return 'G'

def point_sorter((x,y)): return (y,x)

def get_adjacent(grid, location, symbol):
    adjacent = [(location[0] + d[0], location[1] + d[1]) for d in Direction.ALL]
    return [x for x in adjacent if str(grid.get(x,None)) == str(symbol)]

def find_path_to(grid, start, target, max_scan):
    # breadth-first search for target using a tree.
    start_node = AnyNode(location=start)
    frontier = [start_node]
    visited = set()

    while any(frontier):
        node = frontier.pop(0)
        if(max_scan and (node.depth > max_scan)): continue
        if node.location == target:
            return node
        adjacent = [x for x in get_adjacent(grid, node.location, None) if not x in visited]
        # by putting the next frontier items in reading order, we'll choose the correct next path.
        adjacent.sort(key=point_sorter)
        next_nodes = [AnyNode(location=x, parent=node) for x in adjacent]
        visited.add(node.location)
        frontier += next_nodes
    
    #didn't find anything.
    return None

class Direction:
    NORTH = (0,-1)
    EAST = (1,0)
    SOUTH = (0,1)
    WEST = (-1,0)    
    ALL = [NORTH, EAST, SOUTH, WEST]

def manhattan_distance(a, b):
    delta_x = abs(b[0] - a[0])
    delta_y = abs(b[1] - a[1])
    return delta_x + delta_y

def print_grid(grid):
    x_max = max(x[0] for x in grid.keys())
    y_max = max(x[1] for x in grid.keys())
    for y in range(y_max+1):
        for x in range(x_max+1):
            print(grid.get((x,y), '.'), end='')
        print('  ', end='')
        fighters_in_row = [i for i in grid.items() if i[0][1] == y and isinstance(i[1], Fighter)]
        fighters_in_row.sort(key=lambda i:i[0][0])
        print(', '.join(['%s(%s)' % (str(fighter), fighter.hitpoints) for location, fighter in fighters_in_row]))

