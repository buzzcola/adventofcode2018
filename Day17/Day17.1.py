import re, collections
from Shared import *

CLAY = '#'
WATER = '~'
SPRING = '+'
CONDUIT = '|'

with open('input','r') as f: input = f.read()
grid = {}

# populate the grid from the input.
pattern = re.compile(r'^(?P<left_axis>[xy])=(?P<left_number>\d+), (?P<right_axis>[xy])=(?P<right_start>\d+)..(?P<right_end>\d+)$')
for row in input.split('\n'):
    m = pattern.match(row)
    (left_number, right_start, right_end) = [int(m.group(x)) for x in ['left_number', 'right_start', 'right_end']]
    for args in [{m.group('left_axis'): left_number, m.group('right_axis'): x} for x in range(right_start, right_end + 1)]:
        p = Point(**args)
        grid[p] = CLAY

(min_x, min_y), (max_x, max_y) = get_outer_bounds(grid.keys())
can_flow = lambda p: grid.get(p, CONDUIT) == CONDUIT
in_range = lambda p: max_y >= p.y

def print_grid():
    for row in get_rows_in_range(*get_outer_bounds(grid.keys())):
        print ''.join([grid.get(point, '.') for point in row])

# add the spring
spring_point = Point(500,0)
grid[spring_point] = SPRING

# release one drop and flow all the way through. Return true if something was filled.
def drip(start):
    drip_result = False
    frontier = [start]
    visited = {start}
    while any(frontier):
        current = frontier.pop(0)
        grid[current] = CONDUIT
        if not in_range(current.down()): continue
        if can_flow(current.down()):
            frontier.append(current.down())
            visited.add(current.down())
        else:            
            next_points = [x for x in (current.left(), current.right()) if can_flow(x) and x not in visited and in_range(x)]            
            if next_points:
                frontier += next_points
                visited.update(next_points)
            else:
                fill_result = try_fill(current)
                if not fill_result: continue
                drip_result = True
                for filled in fill_result['row']:
                    if filled in frontier: frontier.remove(filled)

                for feeder in fill_result['feeders']:                    
                    next_up = feeder.up()
                    while try_fill(next_up):
                        next_up = next_up.up()                

    return drip_result

# see if a point and its L/R neighbours hold water. If so, fill them and return the conduits that feed the pool.
def try_fill(current):
    bounds = []
    for direction in [Direction.LEFT, Direction.RIGHT]:
        neighbour = current.move(direction)
        while True: 
            if grid.get(neighbour, None) == CLAY: break
            elif can_flow(neighbour.down()): return None
            else: neighbour = neighbour.move(direction)
        bounds.append(neighbour)
    
    row = list(get_points_in_range(Point(bounds[0].x + 1, current.y), Point(bounds[1].x - 1, current.y)))
    for p in row:
        grid[p] = WATER
    
    return {
        'feeders': [p for p in row if grid.get(p.up(), None) == CONDUIT],
        'row': row
    }

# drip drops until everything is filled.
while drip(spring_point.down()): pass

print_grid()
counts = collections.Counter(v for k,v in grid.items() if k.y >= min_y)
print counts[WATER] + counts[CONDUIT]
print counts[WATER]