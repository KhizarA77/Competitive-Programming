def findMinScalar(v1, v2):
    v1.sort()
    v2.sort()
    result = 0
    for i in range(len(v1)):
        result = result + (v1[i]*v2[len(v2)-1-i])

    return result




def main():

    testCases = int(input())
    for i in range(testCases):
        n = int(input())
        _input = input().split(' ')
        _input2 = input().split(' ')
        v1 = [int(numeric_string) for numeric_string in _input]
        v2 = [int(numeric_string) for numeric_string in _input2]
        print(f"Case #{i+1}: {findMinScalar(v1,v2)}")


main()