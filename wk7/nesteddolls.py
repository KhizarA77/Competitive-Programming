
def can_fit(outer, inner):
    return outer[0] > inner[0] and outer[1] > inner[1]

def nested_dolls(dimensions):
    n = len(dimensions)
    dp = [0] * n
    # For each i find all boxes that can be stacked inside it before it. 
    for i in range(1, n):
        S = [dp[j] for j in range(i) if can_fit(dimensions[i], dimensions[j])]
        if S:
            dp[i] = max(S) + 1
    return max(dp)
    
def main():
    T = int(input())
    for _ in range(T):

        m = int(input())
        dolls_data = list(map(int, input().split()))
        dolls = []
        for i in range(0, 2*m-1, 2):
            dolls.append((dolls_data[i], dolls_data[i+1]))
        dolls.sort(key=lambda x: (x[0], -x[1]))
        # print(dolls)
        print(f"max: {nested_dolls(dolls)}")
            
main()