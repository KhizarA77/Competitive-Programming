def main():
    n = int(input())
    
    rev = []
    
    cnv = {}
    
    adj = [[] for _ in range(n)]
    
    for _ in range(n):
        s = input().strip()
        
        v = s.split()
        
        v[0] = v[0][:-1]
        
        for name in v:
            if name not in cnv:
                cnv[name] = len(rev)
                rev.append(name)
        
        n1 = cnv[v[0]]
        for i in range(1, len(v)):
            adj[cnv[v[i]]].append(n1)  
    start = input().strip()
    startidx = cnv[start]
    
    # Count in-degrees (number of dependencies for each file)
    deg = [0] * n
    for i in range(n):
        for j in adj[i]:
            deg[j] += 1
    
    # Find all files with zero in-degree (no dependencies) except the start file
    zeroin = []
    for i in range(n):
        if deg[i] == 0 and i != startidx:
            zeroin.append(i)
    
    # Topological sort to remove irrelevant files
    while zeroin:
        curr = zeroin.pop(0)
        for next_file in adj[curr]:
            deg[next_file] -= 1
            if deg[next_file] == 0 and next_file != startidx:
                zeroin.append(next_file)
    
    # Topological sort for the answer, starting with the changed file
    zeroin = [startidx]
    while zeroin:
        curr = zeroin.pop(0)
        print(rev[curr])
        for next_file in adj[curr]:
            deg[next_file] -= 1
            if deg[next_file] == 0:
                zeroin.append(next_file)
main()