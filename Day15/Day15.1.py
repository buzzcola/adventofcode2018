from Shared import Goblin, Elf, print_grid

with open('input','r') as f: input = f.read()
(ELF, GOBLIN, WALL) = ['E','G','#']
grid = {}
rows = input.split('\n')
for y, row in zip(range(len(rows)), rows):
    for x, char in zip(range(len(row)), row):
        if char == ELF: grid[(x,y)] = Elf()
        elif char == GOBLIN: grid[(x,y)] = Goblin()
        elif char == WALL: grid[(x,y)] = WALL

