with open('input','r') as f: input = f.read() 

player_count = 455
marble_count = 71223

player_scores = [0 for _ in range(player_count)]
marble = 0
marble_ring = [marble]
current_marble_index = 0
current_player = 0

while marble < marble_count:
    marble += 1
    if marble % 23 == 0:
        player_scores[current_player] += marble
        index_to_remove = ((current_marble_index - 7) % len(marble_ring))
        player_scores[current_player] += marble_ring[index_to_remove]        
        del marble_ring[index_to_remove]
        current_marble_index = index_to_remove % len(marble_ring)
    else:
        next_index = ((current_marble_index + 1) % len(marble_ring)) + 1
        marble_ring.insert(next_index, marble)
        current_marble_index = next_index
    
    current_player = (current_player + 1) % player_count

print max(player_scores)