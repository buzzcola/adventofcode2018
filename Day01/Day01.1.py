with open('input','r') as f: input = f.read() 
print sum(int(change) for change in input.split(','))