with open('input','r') as f: input = f.read() 

changes = input.split(',')
frequency = 0
visited = set()
i = 0

while True:        
    visited.add(frequency)

    change = changes[i]
    frequency += int(change[1:]) * (-1 if change[0] == '-' else 1)

    if frequency in visited: 
        break

    i = (i + 1) % len(changes)

print frequency