import os
import math
from collections import Counter
from Shared import *

OPEN = '.'
TREE = '|'
YARD = '#'

with open('input','r') as f: input = f.read()
grid = {}

# populate the grid from the input.
for y, row in enumerate(input.split('\n')):
    for x, char in enumerate(row):
        grid[Point(x,y)] = char

def print_grid():
    for row in get_rows_in_range(*get_outer_bounds(grid.keys())):
        print ''.join([grid[p] for p in row])

(min_x, min_y), (max_x, max_y) = get_outer_bounds(grid.keys())
in_bounds = lambda p: min_x <= p.x <= max_x and min_y <= p.y <= max_y

step = 0
seen = {}
goal = 1000000000
while step < goal:
    next_grid = {}    
    for p in grid:
        char = grid[p]
        counts = Counter(grid[x] for x in p.adjacent() if in_bounds(x))
        if char == OPEN and counts[TREE] >= 3: char = TREE
        elif char == TREE and counts[YARD] >= 3: char = YARD
        elif char == YARD and (counts[YARD] == 0 or counts[TREE] == 0): char = OPEN
        next_grid[p] = char
    grid = next_grid
    step += 1
    key = ''.join(grid.values())
    if key in seen:
        interval = step - seen[key]
        step += interval * math.floor((goal - step) / interval)

    seen[key] = step

counts = Counter(grid.values())
print counts[TREE] * counts[YARD]