# Min height. DP Problem. Use x litres to get max height. 200000

def calculateWater(heights, height):
    waterUsed = 0
    for h in heights:
        if h < height:
            waterUsed = waterUsed + (height - h)
    return waterUsed

def max_height(x, heights):
    heights.sort()
    low = heights[0]
    hi = max(heights) + x
    possible_solutions = set()
    while low <= hi:
        mid = (low+hi) // 2
        water_used = calculateWater(heights, mid)
        if water_used == x:
            return mid
        elif water_used > x:
            hi = mid-1
        else:
            possible_solutions.add(mid)
            low = mid+1
    return max(possible_solutions)


def main():
    T = int(input())
    for _ in range(0, T):
        n, x = map(int, input().split())
        heights = list(map(int, input().split()))
        print(max_height(x, heights))
main()