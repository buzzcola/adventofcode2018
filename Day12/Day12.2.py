with open('input','r') as f: input = f.read() 
start_pots = input.split('\n')[0][15:]
patterns = {row[0:5] for row in input.split('\n')[2:] if row[9] == '#'}

pots = {i:c=='#' for c,i in zip(start_pots, range(len(start_pots)))}
get_pattern = lambda pot_number: ''.join(['#' if pots.get(i, False) else '.' for i in range(pot_number - 2, pot_number + 3)])

last_score = 0
last_delta = 0
remaining = 50000000000

while remaining:
	pots_with_plants = [x[0] for x in pots.items() if x[1]]
	(start_pot_number, end_pot_number) = (min(pots_with_plants) - 2, max(pots_with_plants) + 2)
	pots = {x:(get_pattern(x) in patterns) for x in range(start_pot_number, end_pot_number + 1)}
	score = sum(x[0] for x in pots.items() if x[1])

	delta = score - last_score
	last_score = score
	remaining -= 1
	if delta == last_delta:
		break
	
	last_delta = delta

print last_score + (remaining * last_delta)