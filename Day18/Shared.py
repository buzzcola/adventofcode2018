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
    def move(self, direction): return self + direction
    def adjacent(self):
        for direction in Direction.ALL:
            yield self + direction

class Direction:
    UP = (0,-1)
    RIGHT = (1,0)
    DOWN = (0,1)
    LEFT = (-1,0)
    UP_LEFT = (-1,-1)
    UP_RIGHT = (1,-1)
    DOWN_LEFT = (-1,1)
    DOWN_RIGHT = (1,1)
    ALL = [UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT]

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