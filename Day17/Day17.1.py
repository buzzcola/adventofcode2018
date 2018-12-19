import re
from Shared import *

CLAY = '#'
WATER_FLOWING = '|'
WATER_REST = '~'
SPRING = '+'

with open('input','r') as f: input = f.read()
grid = {}
spring_point = Point(500,0)
grid[spring_point] = SPRING

pattern = re.compile(r'^(?P<left_axis>[xy])=(?P<left_number>\d+), (?P<right_axis>[xy])=(?P<right_start>\d+)..(?P<right_end>\d+)$')
for row in input.split('\n'):
    m = pattern.match(row)
    (left_number, right_start, right_end) = [int(m.group(x)) for x in ['left_number', 'right_start', 'right_end']]
    for args in [{m.group('left_axis'): left_number, m.group('right_axis'): x} for x in range(right_start, right_end + 1)]:
        p = Point(**args)
        grid[p] = CLAY

for row in get_rows_in_range(*get_outer_bounds(grid.keys())):
    print ''.join([grid.get(point, '.') for point in row])


while True:
    # flow the water.
    

    # produce one new unit below the spring.
    grid[spring_point + Direction.DOWN] = WATER_FLOWING
