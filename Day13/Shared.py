import operator
import itertools

class Orientation:
    NORTH = (0,-1)
    EAST = (1,0)
    SOUTH = (0,1)
    WEST = (-1,0)    
    SYMBOLS = {'^':NORTH, '>':EAST, 'v':SOUTH, '<':WEST}

class Rotation:
    RIGHT = 1
    LEFT = -1
    STRAIGHT = 0
    CLOCKWISE = [Orientation.NORTH, Orientation.EAST, Orientation.SOUTH, Orientation.WEST]

class Cart:
    def __init__(self, position, orientation):
        self.position = position
        self.orientation = orientation
        self.intersection_rotations = iter(itertools.cycle([Rotation.LEFT, Rotation.STRAIGHT, Rotation.RIGHT]))
    
    def rotate(self, amount):
        start = Rotation.CLOCKWISE.index(self.orientation)
        result = (start + amount) % len(Rotation.CLOCKWISE)
        self.orientation = Rotation.CLOCKWISE[result]

    def isHorizontal(self):
        return self.orientation in [Orientation.EAST, Orientation.WEST]

    def move(self, track):
        self.position = (self.position[0] + self.orientation[0], self.position[1] + self.orientation[1])
        tile = track[self.position]
        if tile == '\\': self.rotate(Rotation.RIGHT if self.isHorizontal() else Rotation.LEFT)
        elif tile == '/': self.rotate(Rotation.LEFT if self.isHorizontal() else Rotation.RIGHT)
        elif tile == '+': self.rotate(self.intersection_rotations.next())

def print_track(track, carts):
    x_max = max(x[0] for x in track.keys())
    y_max = max(x[1] for x in track.keys())
    cart_symbols = {v:k for k,v in Orientation.SYMBOLS.items()}
    cart_data = {x.position:x for x in carts}
    for y in range(y_max + 1):
        for x in range(x_max + 1):
            if (x,y) in cart_data:
                print cart_symbols[cart_data[(x,y)].orientation],
            else:
                print track[(x,y)],
        print
