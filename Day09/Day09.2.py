from DoublyLinkedList import DoublyLinkedList
with open('input','r') as f: input = f.read() 

player_count = 455
marble_count = 7122300

player_scores = [0 for _ in range(player_count)]
marble = 0
marble_ring = DoublyLinkedList([marble])
current_marble_node = marble_ring.head
current_player = 0

def go_forward(node, x):
    for _ in range(x): node = node.next or marble_ring.head
    return node

def go_backward(node, x):
    for _ in range(x): node = node.previous or marble_ring.tail
    return node

while marble < marble_count:
    marble += 1
    if marble % 23 == 0:
        player_scores[current_player] += marble
        current_marble_node = go_backward(current_marble_node, 7)
        player_scores[current_player] += current_marble_node.data
        node_to_remove = current_marble_node        
        current_marble_node = go_forward(current_marble_node, 1)
        marble_ring.remove(node_to_remove)
    else:
        sibling = go_forward(current_marble_node, 1)
        current_marble_node = marble_ring.insertAfter(sibling, marble)
    
    current_player = (current_player + 1) % player_count

print max(player_scores)