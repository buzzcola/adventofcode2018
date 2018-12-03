import re, itertools
with open('input','r') as f: input = f.read()

ex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
grid = {}

for claim in input.split('\n'):
    (id, x, y, width, height) = (map(int, ex.match(claim).groups()))
    for c in itertools.product(range(x, x + width), range(y, y + height)):
        grid[c] = grid.get(c, 0) + 1

print sum(c > 1 for c in grid.values())