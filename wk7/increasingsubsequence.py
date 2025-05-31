def increasing_subsequence(arr):
    n = len(arr)
    if n == 0:
        return "0"
    
    L = []
    L_id = []
    prev = [-1] * n
    
    for i in range(n):
        pos = binary_search(L, arr[i])
        
        # Update previous index
        if pos > 0:
            prev[i] = L_id[pos-1]
        
        if pos == len(L):
            L.append(arr[i])
            L_id.append(i)
        else:
            if arr[i] < L[pos]:
                L[pos] = arr[i]
                L_id[pos] = i
    
    lis_length = len(L)
    lis = []

    curr = L_id[lis_length - 1]
    
    while curr != -1:
        lis.append(arr[curr])
        curr = prev[curr]
    
    lis.reverse()
    
    return f"{lis_length} {' '.join(map(str, lis))}"

def binary_search(L, target):
    left, right = 0, len(L)
    
    while left < right:
        mid = (left + right) // 2
        if L[mid] >= target:
            right = mid
        else:
            left = mid + 1
    
    return left

def main():
    while True:
        line = input().split()
        n = int(line[0])
        if n == 0:
            break
        arr = list(map(int, line[1:]))
        print(increasing_subsequence(arr))

if __name__ == "__main__":
    main()