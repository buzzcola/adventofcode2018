from Shared import Goblin, Elf, Fighter, print_grid, find_enemies

with open('input','r') as f: input = f.read()
(ELF, GOBLIN, WALL) = ['E','G','#']
grid = {}
rows = input.split('\n')
for y, row in zip(range(len(rows)), rows):
    for x, char in zip(range(len(row)), row):
        if char == ELF: grid[(x,y)] = Elf()
        elif char == GOBLIN: grid[(x,y)] = Goblin()
        elif char == WALL: grid[(x,y)] = WALL

round = 0
while True:    
    goblins_remain = any(type(x) is Goblin for x in grid.values())
    elves_remain = any(type(x) is Elf for x in grid.values())
    if not goblins_remain or not elves_remain:
        break
    
    round += 1
    fighters = [(coord,x) for coord,x in grid.items() if isinstance(x, Fighter)]
    fighters.sort(key=lambda x:x[0]) # sort by coordinates to ensure reading order
    for (location,fighter) in fighters:
        enemy_nodes = find_enemies(grid, location, fighter.enemy)
        if not any(enemy_nodes): continue
        adjacent_enemies = [(x.location, grid[x.location]) for x in enemy_nodes if x.depth == 1]

        # move towards enemy
        if not any(adjacent_enemies):
            target_distance = enemy_nodes.min(key=lambda x:x.depth)
            targets = [x for x in enemy_nodes if x.depth == target_distance]
            next_location = min(x.ancestors[x.depth - 1].location for x in targets)
            del grid[location]
            grid[next_location] = fighter
            enemy_nodes = find_enemies(grid, coord, fighter.enemy)
            adjacent_enemies = [(x.location, grid[x.location]) for x in enemy_nodes if x.depth == 1]
        
        # attack!
        if any(adjacent_enemies):
            adjacent_enemies.sort(key=lambda x:(x[1].hitpoints, x[0]))
            victim = adjacent_enemies[0]
            victim[1].hitpoints -= fighter.attack_power
            if victim[1].hitpoints <= 0:
                # kill!
                del grid[victim[0]]