def solve_shopping_division(items, suspicious_pairs):
    graph = {item: [] for item in items}
    for item1, item2 in suspicious_pairs:
        graph[item1].append(item2)
        graph[item2].append(item1)
    
    colors = {item: -1 for item in items}
    
    # BFS to color the graph
    def is_bipartite():
        for start_item in items:
            if colors[start_item] == -1:
                queue = [start_item]
                colors[start_item] = 0 
                
                while queue:
                    current = queue.pop(0)
                    
                    for neighbor in graph[current]:
                        if colors[neighbor] == -1:
                            colors[neighbor] = 1 - colors[current]
                            queue.append(neighbor)
                        elif colors[neighbor] == colors[current]:
                            return False
        return True
    if is_bipartite():
        walter_items = [item for item in items if colors[item] == 0]
        jesse_items = [item for item in items if colors[item] == 1]
        return walter_items, jesse_items
    else:
        return "impossible"

def main():
    n = int(input())
    items = []
    for _ in range(n):
        items.append(input())
    
    m = int(input())
    suspicious_pairs = []
    for _ in range(m):
        pair = input().split()
        suspicious_pairs.append((pair[0], pair[1]))
    
    result = solve_shopping_division(items, suspicious_pairs)
    
    if result == "impossible":
        print("impossible")
    else:
        walter_items, jesse_items = result
        print(" ".join(walter_items))
        print(" ".join(jesse_items))

if __name__ == "__main__":
    main()