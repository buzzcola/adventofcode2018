import re, itertools
with open('input','r') as f: input = f.read()

ex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
claim_coordinates = {}
for claim in input.split('\n'):
    (id, x, y, width, height) = (map(int, ex.match(claim).groups()))
    claim_coordinates[id] = list(itertools.product(range(x, x + width), range(y, y + height)))

grid = {}
for c in itertools.chain.from_iterable(claim_coordinates.values()):
    grid[c] = grid.get(c, 0) + 1

for (id,coordinates) in claim_coordinates.items():
    if  sum(grid[c] for c in coordinates) == len(coordinates):
        print id
        break