from collections import defaultdict, deque

def solve():
    test_case = 1
    while True:
        try:
            m, n = map(int, input().split())
        except EOFError:
            break
            
        graph = defaultdict(list)
        roads = []
        
        for _ in range(n):
            a, b = map(int, input().split())
            graph[a].append(b)
            roads.append((a, b))
        
        if is_strongly_connected(graph, m):
            print(f"Case {test_case}: valid")
        else:
            found_solution = False
            for a, b in roads:
                graph[a].remove(b)
                graph[b].append(a)
                
                if is_strongly_connected(graph, m):
                    print(f"Case {test_case}: {a} {b}")
                    found_solution = True
                    break
                    
                graph[b].remove(a)
                graph[a].append(b)
            
            if not found_solution:
                print(f"Case {test_case}: invalid")
                
        test_case += 1

def is_strongly_connected(graph, num_nodes):
    for start_node in range(num_nodes):
        visited = [False] * num_nodes
        queue = deque([start_node])
        visited[start_node] = True
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        if not all(visited):
            return False
            
    return True

solve()