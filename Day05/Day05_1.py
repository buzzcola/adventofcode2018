from time import time
from DoublyLinkedList import DoublyLinkedList

def toggle_case(char):
    return char.lower() if char.istitle() else char.upper()

# first try
def react1(polymer):    
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

'''
Second try: build a "virtual map" of the string as a list of indices.
Instead of operating on the string, just remove indices from the list.

Result: Total failure, even slower :( Turns out "del indices[found:found+2]" is about 
the same speed as the massive string operations in the first approach.

Confirmed: https://wiki.python.org/moin/TimeComplexity
Lists are O(n) for insertion and removal.
'''
def react2(polymer):
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

'''
Third try: time for a hand-coded data structure! Couldn't find a library class
for this but i'm sure there's something somewhere on pip.
'''
def react3(polymer):
    d = DoublyLinkedList(list(polymer))
    current = d.head
    while current.next:
        if current.data == toggle_case(current.next.data):
            (kill1, kill2) =  (current, current.next)
            current = current.previous
            d.remove(kill1, kill2)
            if not current: current = d.head
        else:
            current = current.next
    
    return len(list(d.items()))

if __name__ == 'main':
    with open('input','r') as f: input = f.read()

    for function in [react1, react2, react3]:
        start = time()
        print function(input)
        print '%s: %ss' % (function, time() - start)
        
'''
react1: 6.66499996185s
react2: 6.72800016403s
react2: 0.387000083923s
'''