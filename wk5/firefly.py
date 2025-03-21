def findMax(rack1, rack2):

    max1 = 0
    max2 = 0

    for i in range(0, len(rack1)):

        max1 = max(max1, rack1[i])
        max2 = max(max2, rack2[i])

    return max(max1, max2)

def removeElements(rack1, rack2, element):

    val = [x for x in rack1 if x>element]
    val2 = [x for x in rack2 if x>element]

    return (val, val2)


# So we start from mid, we check if we remove mid are all weights in the position we want, if not, we make low = mid+1, otherwise we make high = mid-1. 
def firefly(rack1, rack2):

    low = 0
    hi = findMax(rack1, rack2)
    
    
    while low < hi:

        mid = (low+hi)//2
        _rack1, _rack2 = removeElements(rack1, rack2, mid)

        i = 0
        flag = False
        while(i < len(_rack1)):
            if i+1 >= len(_rack1):
                low = mid+1
                flag = True
                break
            if _rack1[i] != _rack1[i+1]:
                low = mid+1
                flag = True
                break
            i += 2
        i = 0
        if (not flag):
            while (i < len(_rack2)):
                if i+1 >= len(_rack2):
                    low = mid+1
                    flag = True
                    break
                if _rack2[i] != _rack2[i+1]:
                    low = mid+1
                    flag = True
                    break
                i+=2
        if (not flag):
            hi = mid


    
    return low

def main():
    n = int(input())
    rack1 = input().split(' ')
    rack2 = input().split(' ')
    for i in range (0, n):
        rack1[i] = int(rack1[i])
        rack2[i] = int(rack2[i])
    
    print(firefly(rack1, rack2))

main()