import re, itertools
with open('input','r') as f: input = f.read()

ex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
grid = {}

for claim in input.split('\n'):
    (id, x_start, y_start, width, height) = (map(int, ex.match(claim).groups()))
    for x,y in itertools.product(range(x_start, x_start + width), range(y_start, y_start + height)):
        grid[(x,y)] = grid.get((x,y), 0) + 1

print sum(c > 1 for c in grid.values())