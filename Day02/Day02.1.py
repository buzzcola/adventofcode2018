with open('input','r') as f: input = f.read() 
ids = input.split('\n')

(twos, threes) = (0,0)

for id in ids:
    counts = {char : id.count(char) for char in set(id)}
    if any(x == 2 for x in counts.values()): twos += 1
    if any(x == 3 for x in counts.values()): threes += 1  

print twos * threes