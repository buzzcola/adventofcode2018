from itertools import groupby
from Shared import Cart, Orientation, print_track
with open('input','r') as f: input = f.read()
track = {}
carts = []
debug = False

rows = input.split('\n')
for y, row in zip(range(len(rows)), rows):
    for x, char in zip(range(len(row)), row):
        if char in Orientation.SYMBOLS:
            cart = Cart((x,y), Orientation.SYMBOLS[char])
            carts.append(cart)
            track[(x,y)] = '-' if cart.isHorizontal() else '|'
        else:
            track[(x,y)] = char

positions = {x.position for x in carts}

crashed = False
while not crashed:
    if debug:
        print_track(track, carts)
        raw_input('[continue]')
    carts.sort(key=lambda x:x.position) # reset top-left to bottom-right order
    for cart in carts: 
        positions.remove(cart.position)
        cart.move(track)
        if cart.position in positions:
            print 'CRASH! %s,%s' % cart.position
            crashed = True
            break
        positions.add(cart.position)