from math import comb

def solve():
    g = int(input())
    
    for game in range(1, g + 1):
        m = int(input())
        tiles = list(map(int, input().split()))
        
        n, target = map(int, input().split())
        
        dp = [[0] * (n + 1) for _ in range(target + 1)]
        dp[0][0] = 1
        for tile in tiles:
            for j in range(n, 0, -1):
                for subset_sum in range(tile, target + 1):
                    dp[subset_sum][j] = dp[subset_sum][j] + dp[subset_sum - tile][j - 1]
        
        total_ways = comb(m, n)
        favorable = dp[target][n]
        unfavorable = total_ways - favorable
        
        print(f"Game {game} -- {favorable} : {unfavorable}")

solve()