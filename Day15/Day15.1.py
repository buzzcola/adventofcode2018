from Shared import *

debug = False

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
winner = None

if debug: 
    print 'Round %s' % round
    print_grid(grid)
    raw_input('[continue]')

while True: # begin!
        
    fighters = [(coord,x) for coord,x in grid.items() if isinstance(x, Fighter)]
    fighters.sort(key=lambda x:point_sorter(x[0])) # sort by coordinates every time to ensure reading order

    for (location,fighter) in fighters:

        if fighter.hitpoints <= 0:
            continue # he dead     
        
        adjacent_enemies = get_adjacent(grid, location, fighter.enemy)
        
        # move towards enemy
        if not any(adjacent_enemies):
            enemy_locations = [x[0] for x in grid.items() if str(x[1]) == fighter.enemy]

            # is it over?
            if not any(enemy_locations):
                winner = type(fighter)
                round -= 1
                break

            # get all empty tiles adjacent to enemies
            distinct_targets = set()
            for enemy_location in enemy_locations:
                distinct_targets.update(get_adjacent(grid, enemy_location, None))

            # sort targets by distance. closer ones are likelier to be a short path.
            targets = list(distinct_targets)
            targets.sort(key=lambda x: manhattan_distance(location, x))

            # try/get path to enemy adjacents
            paths = []
            shortest = None

            for target in targets:
                # if the manhattan distance is longer than our shortest path,
                # you couldn't get there even with a straight shot, so don't bother.
                if shortest and (manhattan_distance(location, target) > shortest):
                    continue

                path = find_path_to(grid, location, target, shortest)
                if path: 
                    paths.append(path)
                    shortest = path.depth

            # if no paths, end turn
            if not any(paths): continue

            # get shortest paths
            min_length = min(paths, key=lambda x:x.depth).depth
            paths = [x for x in paths if x.depth == min_length]

            # sort by destination's reading order 
            paths.sort(key=lambda x:point_sorter(x.location))

            # move to first location in first path
            next_location = paths[0].path[1].location
            del grid[location]
            grid[next_location] = fighter
            location = next_location
            adjacent_enemies = get_adjacent(grid, location, fighter.enemy)
        
        # attack!
        if any(adjacent_enemies):
            adjacent_enemies.sort(key=lambda x:(grid[x].hitpoints, point_sorter(x)))
            victim_location = adjacent_enemies[0]
            victim = grid[victim_location]
            victim.hitpoints -= fighter.attack_power
            if victim.hitpoints <= 0:
                # kill! kill! kill!
                del grid[victim_location]

        if debug: 
            print '%s round completed' % round
            print_grid(grid)
            raw_input('[continue]')

    round += 1

    print 'round %s:' % round
    goblins = [x for x in grid.values() if type(x) is Goblin]
    elves = [x for x in grid.values() if type(x) is Elf]
    print 'Goblins: %s (%s hp) / Elves: %s (%s hp)' % (
        len(goblins), 
        sum(x.hitpoints for x in goblins),
        len(elves),
        sum(x.hitpoints for x in elves))

    if winner: break

print_grid(grid)
print 'combat completed after %s full rounds.' % round
total_hp = sum(x.hitpoints for x in grid.values() if type(x) is winner)
print 'remaining hp: %s' % total_hp
print 'outcome: %s' % (total_hp * round)