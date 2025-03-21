def generateSequence(n, m, a, c, x0):

    seq = []
    x1 = (a*x0 + c) % m
    seq.append(x1)
    for i in range(1, n):
        x = (a*seq[i-1] + c) % m
        seq.append(x)
    
    return seq

def binarySearch(seq, target):
    low, hi = 0, len(seq) - 1  

    while low <= hi:  
        mid = (low + hi) // 2
        if seq[mid] == target:
            return mid 
        elif target > seq[mid]:
            low = mid + 1
        else:
            hi = mid - 1 

    return low


def outofsorts(n, m, a, c, x0):
    seq = generateSequence(n, m, a, c, x0)

    count = 0

    for num in seq:
        pos = binarySearch(seq, num)
        if pos < len(seq) and seq[pos] == num:
            count += 1

    return count
    


def main():

    _input = input().split(' ')
    n = int(_input[0])
    m = int(_input[1])
    a = int(_input[2])
    c = int(_input[3])
    x0 = int(_input[4])
    print(outofsorts(n, m, a, c, x0))

main()