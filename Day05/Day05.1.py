from time import time
with open('input','r') as f: input = f.read()

#input = 'dabAcCaCBAcCcaDA'

def react(polymer):
    toggle_case = lambda x: x.lower() if x.istitle() else x.upper()
    found = None
    start = 0
    while True:
        for i in range(start, len(polymer) - 1):
            if polymer[i] == toggle_case(polymer[i+1]):
                found = i
                break
        if found <> None:
            polymer = polymer[0:found] + polymer[found+2:]
            start = max(found - 1, 0)
            found = None
        else:
            break
    
    return len(polymer)

def react2(polymer):
    '''
    Try #2: maintain a virtual map of the string as a list of indices.
    Instead of operating on the string, just remove indices from the list.

    Result: Slightly slower :( Turns out "del indices[found:found+2]" is about the same speed
    as snipping and recombining the string.
    '''
    toggle_case = lambda x: x.lower() if x.istitle() else x.upper()
    indices = [x for x in range(len(polymer))]
    found = None
    start = 0
    while True:
        for i in range(start, len(indices)-1):      
            if polymer[indices[i]] == toggle_case(polymer[indices[i+1]]):
                found = i
                break
        if found <> None:
            del indices[found: found + 2]
            start = max(found - 1, 0)
            found = None
        else:
            break
    
    return len(indices)


start = time()
print react(input)
print 'react1: %ss' % (time() - start)

start = time()
print react2(input)
print 'react2: %ss' % (time() - start)