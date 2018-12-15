from __future__ import print_function
from anytree import AnyNode

class Fighter:
    def __init__(self):
        self.hitpoints = 200
        self.attack = 3

    def take_turn(self):
        # search for enemies
        

class BreadthFirstSearch:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.visited = set()
        self.enemy_nodes = []
        self.search(self.start)

    def search(self, coord):
        node = AnyNode(location=coord)
        adjacent = [(coord[0] + d[0], coord[1] + d[1]) for d in Direction.ALL]
        new = [(x,y) for x,y in adjacent if (x,y) not in self.visited]
        empty = [(x,y) for x,y in new if (x,y) not in self.grid]
        enemies = [(x,y) for x,y in new if self.grid[(x,y)] == self.goal]
        self.enemy_nodes += [AnyNode(location = (x,y), parent=node) for x,y in enemies]
        self.visited.update([coord] + enemies)
        if any(self.enemy_nodes):
            return
        for x in empty:
            self.search(x)


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
