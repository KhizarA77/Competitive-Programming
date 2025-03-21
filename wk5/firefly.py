import math

def binarySearch(height, heights):

    low = 0
    hi = len(heights)

    while low < hi:
        mid = (low + hi) // 2
        if height > heights[mid]:
            low = mid+1
        else:
            hi = mid

    return (len(heights) - low)


def obstaclesDestroyed(H, height, stalagmites, stalactites):

    return binarySearch(height, stalagmites) + binarySearch(H-height+1, stalactites)



def firefly(H,stalagmites, stalactites):
    min = math.inf
    count = 0

    for i in range(1, H+1):
        destroyed = obstaclesDestroyed(H, i, stalagmites, stalactites)
        if destroyed < min:
            min = destroyed
            count = 1
        elif min == destroyed:
            count += 1

    return min, count


def main():

    _input = input().split(' ')
    N = int(_input[0])
    H = int(_input[1])

    stalagmites = [] # From floor
    stalactites = [] # From ceiling
    for i in range(0, N):
        if i % 2 == 0:
            stalagmites.append(int(input()))
        else:
            stalactites.append(int(input()))
    stalagmites.sort()
    stalactites.sort()
    print(str(firefly(H,stalagmites, stalactites)).replace('(', '').replace(')','').replace(',',''))

main()
