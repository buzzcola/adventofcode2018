import itertools
with open('input','r') as f: input = f.read() 
ids = input.split('\n')

for pair in itertools.product(ids, ids):
    result = ''.join(['' if x <> y else x for (x,y) in zip(pair[0],pair[1])])
    if len(result) == len(pair[0]) - 1:
        print result
        break