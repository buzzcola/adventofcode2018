import operator
with open('input','r') as f: input = f.read() 
print reduce(operator.add, (int(change) for change in input.split(',')), 0)