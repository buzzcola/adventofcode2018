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

positions = {x.position:x for x in carts}

while len(carts) > 1:
    if debug:
        print_track(track, carts)
        raw_input('[continue]')
    carts.sort(key=lambda x:x.position) # reset top-left to bottom-right order
    for cart in list(carts): # duplicate to avoid modifying list in-loop
        if cart.position not in positions: continue # crash victim
        del positions[cart.position]
        cart.move(track)
        if cart.position in positions:
            victim = positions[cart.position]
            del positions[cart.position]
            carts.remove(cart)
            carts.remove(victim)
        else:
            positions[cart.position] = cart

print carts[0].position