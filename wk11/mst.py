class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
        
        return True

def solve_mst():
    while True:
        line = input().split()
        n, m = map(int, line)
        
        if n == 0 and m == 0:
            break
        
        edges = []
        for _ in range(m):
            u, v, w = map(int, input().split())
            edges.append((w, u, v))
        
        edges.sort()
        
        uf = UnionFind(n)
        mst_edges = []
        total_cost = 0
        
        for w, u, v in edges:
            if uf.find(u) != uf.find(v):
                uf.unite(u, v)
                mst_edges.append((u, v))
                total_cost += w
        
        root = uf.find(0)
        all_connected = all(uf.find(i) == root for i in range(n))
        
        if all_connected and len(mst_edges) == n - 1:
            print(total_cost)
            sorted_edges = []
            for u, v in mst_edges:
                sorted_edges.append((min(u, v), max(u, v)))
            sorted_edges.sort()
            
            for u, v in sorted_edges:
                print(u, v)
        else:
            print("Impossible")

if __name__ == "__main__":
    solve_mst()