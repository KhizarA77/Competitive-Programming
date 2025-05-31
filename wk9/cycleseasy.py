def main():
    t = int(input())
    for tt in range(1, t + 1):
        n, k = map(int, input().split())
        
        g = [[False for _ in range(12)] for _ in range(12)]
        
        for _ in range(k):
            x, y = map(int, input().split())
            x -= 1
            y -= 1
            g[x][y] = True
            g[y][x] = True
        
        vertices = list(range(n))
        
        ans = 0
        import itertools
        for perm in itertools.permutations(vertices[1:]):
            path = [vertices[0]] + list(perm)
            
            ok = True
            for i in range(len(path) - 1):
                if g[path[i]][path[i + 1]]:
                    ok = False
                    break
            
            if g[path[-1]][path[0]]:
                ok = False
            
            if ok:
                ans += 1
        
        print(f"Case #{tt}: {(ans // 2) % 9901}")

if __name__ == "__main__":
    main()