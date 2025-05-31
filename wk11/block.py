import heapq

def solve():
    board = [[0 for _ in range(m)] for _ in range(n+2)]
    dist = [[float('inf') for _ in range(m)] for _ in range(n+2)]
    par = [[(float('inf'), float('inf')) for _ in range(m)] for _ in range(n+2)]
    
    for i in range(1, n+1):
        row = input()
        for j in range(m):
            board[i][j] = int(row[j])
    
    dist[0][0] = 0
    q = [(0, (0, 0))]
    
    while q:
        _, (currx, curry) = heapq.heappop(q)
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                nextx = currx + i
                nexty = curry + j
                
                if not inrange(nextx, nexty):
                    continue
                    
                if dist[currx][curry] + board[nextx][nexty] < dist[nextx][nexty]:
                    dist[nextx][nexty] = dist[currx][curry] + board[nextx][nexty]
                    heapq.heappush(q, (-dist[nextx][nexty], (nextx, nexty)))
                    par[nextx][nexty] = (currx, curry)
    
    currx, curry = n+1, m-1
    while currx != float('inf') and curry != float('inf'):
        board[currx][curry] = ord(' ') - ord('0')
        currx, curry = par[currx][curry]
    
    for i in range(1, n+1):
        for j in range(m):
            print(chr(board[i][j] + ord('0')), end='')
        print()
    print()

def inrange(x, y):
    return 0 <= x < n+2 and 0 <= y < m

while True:
    try:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        solve()
    except EOFError:
        break