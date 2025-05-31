def max_profit(times, profits):
    n = len(times)
    if n == 0:
        return "no profit"
    
    dp = [0] * n
    dp[0] = profits[0] - 0.08  
    start_fresh = [True] * n
    
    for i in range(1, n):
        fresh_profit = profits[i] - 0.08
        
        time_diff = times[i] - times[i-1]
        operating_cost = time_diff * 0.08
        continue_profit = dp[i-1] + profits[i] - operating_cost
        
        if fresh_profit >= continue_profit:
            dp[i] = fresh_profit
            start_fresh[i] = True
        else:
            dp[i] = continue_profit
            start_fresh[i] = False
    
    max_profit_value = max(dp)
    
    # Check if profitable
    if max_profit_value <= 0:
        return "no profit"
    
    # Find all indices with maximum profit
    max_indices = [i for i in range(n) if dp[i] == max_profit_value]
    
    # For each max index, find the optimal period
    best_start = -1
    best_end = -1
    best_duration = float('inf')
    
    for end_idx in max_indices:
        # Find start of this profitable period
        start_idx = end_idx
        while start_idx > 0 and not start_fresh[start_idx]:
            start_idx -= 1
        
        start_time = times[start_idx]
        end_time = times[end_idx]
        duration = end_time - start_time
        
        # Choose based on: shortest duration, then earliest start
        if duration < best_duration or (duration == best_duration and start_time < best_start):
            best_start = start_time
            best_end = end_time
            best_duration = duration
    
    return f"{max_profit_value:.2f} {best_start} {best_end}"



def main():

    while True:
        n = int(input())
        if n == 0:
            break
        times = []
        profits = []
        for _ in range(n):
            _input = input().split(' ')
            times.append(int(_input[0]))
            profits.append(float(_input[1]))
        dp = max_profit(times, profits)
        print(dp)
main()