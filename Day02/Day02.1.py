with open('input','r') as f: input = f.read() 
ids = input.split('\n')

counts = [{id.count(char) for char in set(id)} for id in ids]
twos = sum(2 in x for x in counts)
threes = sum(3 in x for x in counts)

print twos * threes