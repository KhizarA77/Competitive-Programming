def numOfSwaps(students):
    swaps = 0
    for i in range(len(students)):
        for j in range(i+1, len(students)):
            if students[i] > students[j]:
                swaps += 1
    return swaps


def main():
    n = int(input())
    students = []

    for i in range(n):
        students.append(int(input()))

    print(numOfSwaps(students))


main()