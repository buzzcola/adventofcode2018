with open('input','r') as f: input = f.read() 
start_pots = input.split('\n')[0][15:]
patterns = {row[0:5] for row in input.split('\n')[2:] if row[9] == '#'}

pots = {i for c,i in zip(start_pots, range(len(start_pots))) if c == '#'}
get_pattern = lambda pot_number: ''.join(['#' if i in pots else '.' for i in range(pot_number - 2, pot_number + 3)])

for _ in range(20):	
	(start_pot_number, end_pot_number) = (min(pots) - 2, max(pots) + 2)
	pots = {i for i in range(start_pot_number, end_pot_number + 1) if get_pattern(i) in patterns}

print sum(pots)