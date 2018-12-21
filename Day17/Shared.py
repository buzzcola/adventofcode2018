from collections import namedtuple
import itertools

PointBase = namedtuple('PointBase', 'x y')
class Point(PointBase):
    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])
    
    def down(self): return self + Direction.DOWN
    def up(self): return self + Direction.UP
    def left(self): return self + Direction.LEFT
    def right(self): return self + Direction.RIGHT

class Direction:
    UP = (0,-1)
    RIGHT = (1,0)
    DOWN = (0,1)
    LEFT = (-1,0)
    ALL = [UP, RIGHT, DOWN, LEFT]

# (Point, Point) top left and bottom right bounds given a list of points.
def get_outer_bounds(points):
    p_iter = iter(points)
    first = p_iter.next()
    (min_x, max_x, min_y, max_y) = (first.x, first.x, first.y, first.y)
    for p in p_iter:
        (min_x, min_y, max_x, max_y) = [min(min_x, p.x), min(min_y, p.y), max(max_x, p.x), max(max_y, p.y)]
    return (Point(min_x, min_y), Point(max_x, max_y))

def get_points_in_range(top_left, bottom_right):
    for y in range(top_left.y, bottom_right.y + 1):
        for x in range(top_left.x, bottom_right.x + 1):
            yield Point(x,y)

def get_rows_in_range(top_left, bottom_right):
    for y in range(top_left.y, bottom_right.y + 1):
        yield [Point(x,y) for x in range(top_left.x, bottom_right.x + 1)]