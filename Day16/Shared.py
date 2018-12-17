from collections import namedtuple

# learned about namedtuple today. Very neat.
Instruction = namedtuple('Instruction', ['opcode', 'a', 'b', 'c'])

class Test:
    def __init__(self, text):
        lines = text.split('\n')
        self.op_number = int(lines[1].split(' ')[0])
        self.args = map(int, lines[1].split(' ')[1:])
        self.before =  map(int, lines[0][9:19].split(','))
        self.after =  map(int, lines[2][9:19].split(','))

class Machine(object):
    def __init__(self):
        self.registers = [0,0,0,0]

    def execute(self, i):
        self.registers[i.c] = getattr(self, i.opcode)(i.a, i.b)
        
    def opcodes(self):
        return [x for x in dir(self) if len(x) == 4] # yup, hacky

    # there is a way to abstract the operator for the first three characters
    # and use the r/i at the end of the instructions to generalize this stuff...
    # I got about halfway through a clever solution before deciding this was
    # much simpler.

    #Addition

    # addr(add register) stores into register C the result of adding register A and register B.
    def addr(self, a, b): return self.registers[a] + self.registers[b]
    #addi (add immediate) stores into register C the result of adding register A and value B.
    def addi(self, a, b): return self.registers[a] + b

    #Multiplication:

    #mulr (multiply register) stores into register C the result of multiplying register A and register B.
    def mulr(self, a, b): return self.registers[a] * self.registers[b]
    #muli (multiply immediate) stores into register C the result of multiplying register A and value B.
    def muli(self, a, b): return self.registers[a] * b

    #Bitwise AND:

    #banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
    def banr(self, a, b): return self.registers[a] & self.registers[b]
    #bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
    def bani(self, a, b): return self.registers[a] & b

    #Bitwise OR:

    #borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
    def borr(self, a, b): return self.registers[a] | self.registers[b]
    #bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
    def bori(self, a, b): return self.registers[a] | b

    #Assignment:

    #setr (set register) copies the contents of register A into register C. (Input B is ignored.)
    def setr(self, a, b): return self.registers[a]
    #seti (set immediate) stores value A into register C. (Input B is ignored.)
    def seti(self, a, b): return a
    
    #Greater-than testing:

    #gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
    def gtir(self, a, b): return int(a > self.registers[b])
    #gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
    def gtri(self, a, b): return int(self.registers[a] > b)
    #gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
    def gtrr(self, a, b): return int(self.registers[a] > self.registers[b])
    
    #Equality testing:
    
    #eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
    def eqir(self, a, b): return int(a == self.registers[b])
    #eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
    def eqri(self, a, b): return int(self.registers[a] == b)
    #eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
    def eqrr(self, a, b): return int(self.registers[a] == self.registers[b])