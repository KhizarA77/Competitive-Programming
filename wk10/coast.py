def main():
    n,m = map(int, input().split())
    arr = []
    for _ in range(n):
        line = [int(x) for x in input().strip()]
        arr.append(line)
    getCoast(n,m,arr)
        
def getCoast(n, m, arr):
    coast = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                if i == 0 or arr[i-1][j] == 0:
                    coast += 1
                if i == n-1 or arr[i+1][j] == 0:
                    coast += 1
                if j == 0 or arr[i][j-1] == 0:
                    coast += 1
                if j == m-1 or arr[i][j+1] == 0:
                    coast += 1

    def flood_fill(x, y, visited):
        stack = [(x, y)]
        is_lake = True
        lake_edges = 0
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 0 and (nx, ny) not in visited:
                        stack.append((nx, ny))
                    elif arr[nx][ny] == 1:
                        lake_edges += 1
                else:
                    is_lake = False
        return is_lake, lake_edges
    
    visited = set()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 and (i, j) not in visited:
                is_lake, lake_edges = flood_fill(i, j, visited)
                if is_lake:
                    coast -= lake_edges

    print(coast)
main()