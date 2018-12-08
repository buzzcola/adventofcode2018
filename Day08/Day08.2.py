with open('input','r') as f: input = f.read() 

class Node:
    def __init__(self, parent, child_count, metadata_count):
        self.parent = parent
        self.child_count = child_count
        self.metadata_count = metadata_count
        self.children = []
        self.metadata = []

    @staticmethod
    def parse(stack, parent = None):
        node = Node(parent, stack.pop(), stack.pop())            
        node.children = [Node.parse(stack, node) for _ in range(node.child_count)]
        node.metadata = [stack.pop() for _ in range(node.metadata_count)]        
        return node

    def get_value(self):
        if not any(self.children): return sum(self.metadata)
        valid_metadata = [x for x in self.metadata if 0 < x <= len(self.children)]
        return sum([self.children[x - 1].get_value() for x in valid_metadata])

stack = map(int, reversed(input.split(' ')))
root = Node.parse(stack)
print root.get_value()