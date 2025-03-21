def sum(subset):
    sum = 0
    for i in subset:
        sum += i
    return sum

smallSum = 0

def makeFruitBaskets(nums, cursum):
    if cursum >= 200:
        return
    global smallSum
    if len(nums) == 0:
        if cursum < 200:
            smallSum += cursum
        return

    makeFruitBaskets(nums[1:], cursum)
    makeFruitBaskets(nums[1:], cursum + nums[0])

def main():
    global smallSum
    n = int(input())
    fruitWeights = list(map(int, input().split(' ')))
    totalWeight = 2**(n-1) * sum(fruitWeights)
    makeFruitBaskets(fruitWeights, 0)
    print(totalWeight - smallSum)

main()