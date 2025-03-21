
def setSum(inputSet):
    return sum(inputSet)

def powerset(A):
    def helper(idx, partial):
        if idx == len(A):
            result.append(partial)
            return
        helper(idx+1, partial)             # Do not include the current value
        helper(idx+1, partial + [A[idx]])  # Include the current value
    result = []
    helper(0, [])
    return result

def equalSum(subsets):

    for i in range(1, len(subsets)):
        for j in range(i+1, len(subsets)):

            if setSum(subsets[i]) == setSum(subsets[j]):
                return (subsets[i],subsets[j])
    return None
   


def main():
    T = int(input())
    for i in range(T):
        _input = input().split(' ')
        nums = []
        for j in range(1, 21):
            nums.append(int(_input[j]))
        subsets = powerset(nums)
        result = equalSum(subsets)
        print(f"Case #{i+1}:")
        if result:
            SetA, SetB = result
            print(" ".join(map(str, SetA)))
            print(" ".join(map(str, SetB)))
        else:
            print("Impossible")
main()