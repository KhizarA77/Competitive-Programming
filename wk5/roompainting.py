def binarySearch(canSizes,target):
    low, hi = 0, len(canSizes) - 1  

    while low <= hi:  
        mid = (low + hi) // 2
        if canSizes[mid] == target:
            return target 
        elif target > canSizes[mid]:
            low = mid + 1
        else:
            hi = mid - 1 

    return canSizes[low]



def findRemainder(canSizes, litresNeeded):

    remainder = 0

    for litre in litresNeeded:
        canSize = binarySearch(canSizes, litre)
        remainder += canSize - litre

    return remainder



def main():

    _input = input().split(' ')
    n = int(_input[0]) # Paints offered
    m = int(_input[1]) # Joes need

    canSizes = []
    for _ in range(n):
        canSizes.append(int(input()))

    litresNeeded = []
    for _ in range(m):
        litresNeeded.append(int(input()))
    
    canSizes.sort()

    print(findRemainder(canSizes, litresNeeded))

main()