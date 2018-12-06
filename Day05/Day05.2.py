with open('input','r') as f: input = f.read()

def react(polymer):
    toggle_case = lambda x: x.lower() if x.istitle() else x.upper()
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
    
    return polymer


results = []
for char in (chr(x) for x in range(ord('a'), ord('z'))):
    result = (char, len(react(input.replace(char,'').replace(char.upper(),''))))
    print '%s: %s' % result
    results.append(result)

best = max(results, key=lambda x: x[1])
print 'best: %s (%s)' % results[0]
