with open('input','r') as f: input = f.read() 
ids = input.split('\n')

(twos, threes) = (0,0)

def getDupes(id):
    letters = {}
    for c in id:
        if letters.has_key(c): letters[c] += 1
        else: letters[c] = 1
    
    return (
        any(x == 2 for x in letters.values()),
        any(x == 3 for x in letters.values())
    )

for id in ids:
    (has_two, has_three) = getDupes(id)
    (twos, threes) = (twos + has_two, threes + has_three)

print twos * threes