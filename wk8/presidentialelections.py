import math

def solve_election(states):
    maximum_delegates = 2016
    total_delegates = 0
    n = len(states)
    
    dp = [[math.inf] * (maximum_delegates + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(n):
        delegates, cons, fed, und = states[i]
        total_delegates += delegates
        
        votes_needed = ((cons + fed + und) // 2) + 1 - cons
        
        for j in range(maximum_delegates + 1):
            if dp[i][j] != math.inf:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
                
                if votes_needed <= und: 
                    if votes_needed <= 0 and j + delegates <= maximum_delegates:
                        dp[i + 1][j + delegates] = min(dp[i + 1][j + delegates], dp[i][j])
                    elif j + delegates <= maximum_delegates:
                        dp[i + 1][j + delegates] = min(dp[i + 1][j + delegates], dp[i][j] + votes_needed)
    
    needed_delegates = (total_delegates // 2) + 1
    
    min_votes = math.inf
    for i in range(needed_delegates, maximum_delegates + 1):
        min_votes = min(min_votes, dp[n][i])
    
    if min_votes == math.inf:
        return "Impossible"
    return min_votes

def main():
    s = int(input())
    states = []
    for _ in range(s):
        d, c, f, u = map(int, input().split())
        states.append((d, c, f, u))
    
    result = solve_election(states)
    print(result)

if __name__ == "__main__":
    main()