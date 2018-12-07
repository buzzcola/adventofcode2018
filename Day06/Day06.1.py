from itertools import product, groupby
with open('input','r') as f: input = f.read() 

# make the list of points as a set. 
coords = {(int(x),int(y)) for x,y in [line.split(',') for line in input.split('\n')]}

# virtual bounding box of all coordinates with an extra 1-width border.
# anything that gets a point the border will be infinite. (right?) (turns out, yes)
top_left = (min(x[0] for x in coords)-1, min(x[1] for x in coords)-1)
bottom_right = (max(x[0] for x in coords)+1, max(x[1] for x in coords)+1)
width = bottom_right[0] - top_left[0] + 1
height = bottom_right[1] - top_left[1] + 1

def distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

# holds the "map" from the question, as a dictionary of (x,y) => closest|None
points = {} 

# for each point in the bounding box, compute distance to all points, save point or None.
for (x,y) in product(range(top_left[0], bottom_right[0]+1), range(top_left[1], bottom_right[1]+1)):
    distances = [(coord, distance((x,y), coord)) for coord in coords]
    min_distance = min(distances, key=lambda x:x[1])[1]
    min_coords = [d[0] for d in distances if d[1] == min_distance]
    points[(x,y)] = min_coords[0] if len(min_coords) == 1 else None

# build a set comprehension of the infinite points (anybody who got a spot on the border)
# and take the "difference" from the original set (which uses the subract operator, cool.)
finite = coords - {
    points[coord] for coord in points if 
        coord[0] in [top_left[0], bottom_right[0]]
        or coord[1] in [top_left[1], bottom_right[1]]
}

# compute scores for remaining (finite) ranges.
scores = [(coord, len([x for x in points.values() if x == coord])) for coord in finite]

winner = max(scores, key=lambda x:x[1])
print 'winner is point %s with %s' % winner