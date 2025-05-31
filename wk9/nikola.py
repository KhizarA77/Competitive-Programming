from heapq import heappush, heappop

def solve_game():
    num_squares = int(input())
    fees = [int(input()) for _ in range(num_squares)]
    
    
    
    priority_queue = [(fees[1], 1, 1)]
    
    explored = set()
    
    while priority_queue:
        total_cost, position, last_jump = heappop(priority_queue)
        
        if position == num_squares - 1:
            return total_cost
            
        if (position, last_jump) in explored:
            continue
            
        explored.add((position, last_jump))
        
        back_pos = position - last_jump
        if back_pos >= 0:
            heappush(priority_queue, (total_cost + fees[back_pos], back_pos, last_jump))
        
        forward_pos = position + last_jump + 1
        if forward_pos < num_squares:
            heappush(priority_queue, (total_cost + fees[forward_pos], forward_pos, last_jump + 1))
    
    return -1

print(solve_game())