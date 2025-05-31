import math

[10, 30, 60]
[20, 30, 10]


def solve(k, l1, r1, l2, r2):
    """
    Count the number of ordered pairs (x,y) such that:
    - l1 ≤ x ≤ r1
    - l2 ≤ y ≤ r2
    - y = x * k^n for some non-negative integer n
    """
    # Special case: k = 1
    if k == 1:
        # When k = 1, y = x, so we need pairs where x = y is in both ranges
        overlap_start = max(l1, l2)
        overlap_end = min(r1, r2)
        return max(0, overlap_end - overlap_start + 1)
    
    count = 0
    
    # For each power n
    n = 0
    k_power = 1  # k^n
    
    while True:
        # For a given n, find x values such that:
        # l2 ≤ x*k^n ≤ r2
        
        # Calculate the range of valid x values for this n
        if l2 <= 0:
            x_min = l1  # Any x in range works for lower bound if l2 ≤ 0
        else:
            x_min = math.ceil(l2 / k_power)
            
        x_max = math.floor(r2 / k_power)
        
        # Restrict to the given x range [l1, r1]
        x_min = max(x_min, l1)
        x_max = min(x_max, r1)
        
        # If there are valid x values for this n, add them to the count
        if x_min <= x_max:
            count += x_max - x_min + 1
        
        # Termination conditions:
        # 1. If all future powers will produce y > r2
        if l1 > 0 and k_power > r2 // l1:
            break
            
        # 2. If k_power might overflow with next multiplication
        if k > 1 and k_power > 10**18 // k:
            break
        
        # Move to the next power
        n += 1
        k_power *= k
    
    return count

def main():
    t = int(input())
    for _ in range(t):
        k, l1, r1, l2, r2 = map(int, input().split())
        print(solve(k, l1, r1, l2, r2))

if __name__ == "__main__":
    main()