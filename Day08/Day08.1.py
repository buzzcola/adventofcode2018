with open('input','r') as f: input = f.read() 

def parse_node(stack):
    child_count = stack.pop()
    metadata_count = stack.pop()
    metadata_total = sum([parse_node(stack) for _ in range(child_count)])
    metadata_total += sum([stack.pop() for _ in range(metadata_count)])
    return metadata_total

stack = map(int, reversed(input.split(' ')))
print parse_node(stack)

