def solve_restaurant_orders():
    dp = [-2] * 32000
    dp[0] = 0
    
    n = int(input())
    
    costs = list(map(int, input().split()))
    
    for i in range(n):
        cost = costs[i]
        for j in range(30001):
            if j + cost >= 32000:
                continue
                
            if dp[j] >= 0:
                if dp[j + cost] == -2:
                    dp[j + cost] = i
                else:  
                    dp[j + cost] = -1
            
            if dp[j] == -1:
                dp[j + cost] = -1  
    
    q = int(input())
    
    orders = list(map(int, input().split()))
    for order in orders:
        process_order(dp, costs, order)

def process_order(dp, costs, order):
    ans = []
    
    if dp[order] == -2:
        print("Impossible")
        return
    
    if dp[order] == -1:
        print("Ambiguous")
        return
    
    while order > 0:
        ans.append(dp[order] + 1)  
        order -= costs[dp[order]]
    
    if order < 0:
        print("Ambiguous")
        return
    
    ans.sort()
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve_restaurant_orders()