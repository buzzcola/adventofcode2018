with open('input','r') as f: input = f.read() 

frequency = 0

for change in input.split(','):
    frequency += int(change[1:]) * (-1 if change[0] == '-' else 1)

print frequency