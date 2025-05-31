from math import log10, inf
from queue import PriorityQueue

def dijikstra(adj):
    dist = [inf] * len(adj)
    dist[0] = 0
    pq = PriorityQueue()
    pq.put((0,0))
    visited = [False] * len(adj)
    while not pq.empty():
        d, u = pq.get()
        
        if visited[u]:
            continue
        
        visited[u] = True
        
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pq.put((dist[v], v))

    res = dist[-1]
    res = -1 * res
    return format(10 ** res, '.4f')

def main():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u, v, w = map(float, input().split())
            u, v = int(u), int(v)
            w = -log10(w)
            adj[u].append((v,w))
            adj[v].append((u,w))
        print(dijikstra(adj))

main()