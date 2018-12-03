import itertools
with open('input','r') as f: input = f.read() 
ids = input.split('\n')

for left,right in itertools.product(ids, ids):
    result = ''.join(['' if c1 <> c2 else c1 for (c1,c2) in zip(left, right)])
    if len(result) == len(left) - 1:
        print result
        break