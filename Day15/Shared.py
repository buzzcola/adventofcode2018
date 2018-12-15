from __future__ import print_function
from anytree import AnyNode, RenderTree

class Fighter(object):
    def __init__(self):
        self.hitpoints = 200
        self.attack_power = 3

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

def find_enemies(grid, start, goal):
    start_node = AnyNode(location=start)
    frontier = [start_node]
    visited = set()
    enemy_nodes = []
    while any(frontier):
        node = frontier.pop(0)
        coord = node.location
        adjacent = [(coord[0] + d[0], coord[1] + d[1]) for d in Direction.ALL]            
        enemies = [(x,y) for x,y in adjacent if grid.get((x,y), None) == goal]
        next_nodes = [AnyNode(location=(x,y), parent=node) for x,y in adjacent if (x,y) not in grid and (x,y) not in visited]
        enemy_nodes += [AnyNode(location = (x,y), parent=node) for x,y in enemies]
        visited.update([coord])
        frontier += next_nodes
    
    return enemy_nodes

class Direction:
    NORTH = (0,-1)
    EAST = (1,0)
    SOUTH = (0,1)
    WEST = (-1,0)    
    ALL = [NORTH, EAST, SOUTH, WEST]

def print_grid(grid):
    x_max = max(x[1] for x in grid.keys())
    y_max = max(x[0] for x in grid.keys())
    for y in range(y_max+1):
        for x in range(x_max+1):
            print(grid.get((x,y), '.'), end='')
        print()
