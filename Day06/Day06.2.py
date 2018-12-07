import numpy
with open('input','r') as f: input = f.read() 

coords = {(int(x),int(y)) for x,y in [line.split(',') for line in input.split('\n')]}

# virtual bounding box of all coordinates with an extra 1-width border.
# anything that gets a point the border will be infinite. right? (turns out, yes)
top_left = (min(x[0] for x in coords)-1, min(x[1] for x in coords)-1)
bottom_right = (max(x[0] for x in coords)+1, max(x[1] for x in coords)+1)
width = bottom_right[0] - top_left[0] + 1
height = bottom_right[1] - top_left[1] + 1

def distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

points = {} # (x,y) -> point "score" (sum of distances)
safe_square_count = 0
for (x,y) in [(x + top_left[0],y + top_left[1]) for (x,y) in numpy.ndindex(width, height)]:
    point_score = sum(distance((x,y), coord) for coord in coords)
    if point_score < 10000: safe_square_count += 1

print 'found safe squares: %s' % safe_square_count