def longest_train(n, weights):
    lis = [1] * n
    lds = [1] * n
    
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if weights[j] > weights[i]:
                lis[i] = max(lis[i], lis[j] + 1)
            if weights[j] < weights[i]:
                lds[i] = max(lds[i], lds[j] + 1)
    
    ans = 0
    for i in range(n):
        ans = max(ans, lis[i] + lds[i] - 1)
    
    return ans

n = int(input())
weights = []
for _ in range(n):
    weights.append(int(input()))

result = longest_train(n, weights)
print(result)