import re, itertools

class Point:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
    
    def next(self):
        new_x = self.position[0] + self.velocity[0]
        new_y = self.position[1] + self.velocity[1]
        return Point((new_x, new_y), self.velocity)


def solve():
    with open('input','r') as f: input = f.read() 
    starting_particles = []
    for match in re.finditer(r'position=<([\d\- ]+),([\d\- ]+)> velocity=<([\d\- ]+),([\d\- ]+)>', input):
        (x, y, x_velocity, y_velocity) = [int(match.group(x + 1)) for x in range(4)]
        starting_particles.append(Point((x, y), (x_velocity, y_velocity)))

    seconds = 0
    particles = starting_particles
    while True:
        result = printPattern(particles)
        if result: 
            input = raw_input('result from second %s:' % seconds)
            if input == 'q': break
        particles = [p.next() for p in particles]
        seconds += 1    

def printPattern(particles):

    (left, top) = (particles[0].position)
    (right, bottom) = (particles[0].position)
    for p in particles:
        (left, top) = (min(left, p.position[0]), min(top, p.position[1]))
        (right, bottom) = (max(right, p.position[0]), max(bottom, p.position[1]))

    # skip printing for large patterns.
    if((right - left) > 100 or (bottom - top) > 100): return False

    positions = set(p.position for p in particles)
    for (y,x) in itertools.product(range(top, bottom + 1), range(left, right + 1)):
        pixel = '#' if (x,y) in positions else '.'
        print pixel,
        if x == right:
            print
    return True

if __name__ == '__main__': solve()