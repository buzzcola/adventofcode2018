from Shared import *
import operator

with open('input','r') as f: input = f.read()
first_half = input.split('\n\n\n\n')[0]
tests = [Test(x) for x in first_half.split('\n\n')]
machine = Machine()
three_plus_tests = 0

for test in tests:
    passing = 0
    for op in machine.opcodes():
        machine.registers = list(test.before)
        machine.execute(Instruction(op, *test.args))
        passing += (machine.registers == test.after)
        if passing == 3:
            three_plus_tests += 1
            break

print three_plus_tests