from Shared import *
import operator

with open('input','r') as f: input = f.read()
(test_data, real_data) = input.split('\n\n\n\n')
tests = [Test(x) for x in test_data.split('\n\n')]
machine = Machine()
candidates = {x:machine.opcodes() for x in range(len(machine.opcodes()))}

# eliminate opcodes from the lists by executing each test.
for test in tests:
    if len(candidates[test.op_number]) == 1: continue
    for op in candidates[test.op_number]:
        machine.registers = list(test.before)
        machine.execute(Instruction(op, *test.args))        
        if machine.registers <> test.after:
            candidates[test.op_number].remove(op)

# eliminate remaining codes by working backwards from 
# confirmed codes (those that were reduced to one candidate.)
while any([len(x) > 1 for x in candidates.values()]):
    for confirmed_number, confirmed_code in [(k,v[0]) for k,v in candidates.items() if len(v) == 1]:
        for op_number, op_codes in candidates.items():
            if op_number == confirmed_number: continue
            if confirmed_code in op_codes: op_codes.remove(confirmed_code)

# execute the code!
machine.registers = [0,0,0,0]
for line in real_data.split('\n'):
    (op_number, a, b, c) = map(int, line.split(' '))
    instruction = Instruction(candidates[op_number][0], a, b, c)
    machine.execute(instruction)

print machine.registers[0]