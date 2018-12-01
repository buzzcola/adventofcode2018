from itertools import cycle
with open('input','r') as f: input = f.read() 

changes = cycle(int(x) for x in input.split(','))
frequency = 0
visited = set()

for change in changes:
    visited.add(frequency)
    frequency += change

    if frequency in visited: 
        break

print frequency