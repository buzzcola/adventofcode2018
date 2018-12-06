from Day05_1 import react1, react2, react3
from time import time

with open('input','r') as f: input = f.read()

for function in [react1, react2, react3]:
    start = time()
    results = []
    for char in (chr(x) for x in range(ord('a'), ord('z')+1)):
        results.append((char, function(input.replace(char,'').replace(char.upper(),''))))

    best = min(results, key=lambda x: x[1])
    elapsed = time() - start
    print 'best: %s (%s)' % best
    print 'time for %s: %ss' % (function, time() - start)

'''
best: s (5726)
time for <function react1 at 0x000000000302FEB8>: 255.062999964s
best: s (5726)
time for <function react2 at 0x000000000302FF28>: 314.249000072s
best: s (5726)
time for <function react3 at 0x000000000302FF98>: 9.90700006485s
'''