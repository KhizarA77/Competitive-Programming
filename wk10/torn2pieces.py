def path(source, destination, adj):
    stack = [(source, [source])]
    visited = set()
    
    while stack:
        node, path_so_far = stack.pop()
        
        if node == destination:
            print(" ".join(path_so_far))
            return
        
        if node not in visited:
            visited.add(node)
            neighbors = list(adj[node])
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append((neighbor, path_so_far + [neighbor]))


def dfs(source, destination, adj):
    stack = [source]
    visited = set()
    while stack:
        node = stack.pop()
        if node == destination:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in adj[node]:
                stack.append(neighbor)
    return False


def main():
    N = int(input())
    adj = dict()
    for _ in range(N):
        _input = input().split()
        if _input[0] not in adj:
            adj[_input[0]] = set()
        for i in range(1, len(_input)):
            adj[_input[0]].add(_input[i])
            if _input[i] not in adj:
                adj[_input[i]] = set()
            adj[_input[i]].add(_input[0])
    source, destination = input().split() 
    
    if source not in adj or destination not in adj:
        print("no route found")
        return
        
    if dfs(source, destination, adj):
        path(source, destination, adj)
    else:
        print("no route found")
        
main()