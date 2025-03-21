import math as Math

possibilities = set()

def generatePossibilities(digit, num):
    
    global possibilities

    if num > 200:
        return

    if digit == 1 or digit == 4 or digit == 2 or digit == 5: # 1, 2, 4, 5
        generatePossibilities(digit+1, num) # Not included
        generatePossibilities(digit+3, num)
        num = num*10 + digit
        if num <= 200:
            possibilities.add(num)
        generatePossibilities(digit, num) # Included
        generatePossibilities(digit+1, num)
        generatePossibilities(digit+3, num)
    
    if digit == 8:
        generatePossibilities(9, num)
        generatePossibilities(0, num)
        num = num*10 + digit
        if num <= 200:
            possibilities.add(num)
        generatePossibilities(8, num)
        generatePossibilities(9, num)
        generatePossibilities(0, num)

    if digit == 7:
        generatePossibilities(8, num)
        num = num*10 + digit
        if num <= 200:
            possibilities.add(num)
        generatePossibilities(7, num)
        generatePossibilities(8, num)


    if digit == 3 or digit == 6:
        generatePossibilities(digit+3, num)
        num = num*10 + digit
        if num <= 200:
            possibilities.add(num)
        generatePossibilities(digit, num)
        generatePossibilities(digit+3, num)

    if digit == 9:
        num = num*10 + digit
        if num <= 200:
            possibilities.add(num)
        generatePossibilities(9, num)

    if digit == 0:
        num = num*10 + digit
        if num <= 200:
            possibilities.add(num)
        if num != 0:
            generatePossibilities(0, num)


def main():
    generatePossibilities(1, 0)
    global possibilities
    possibilities = list(possibilities)
    possibilities.sort()
    
    n = int(input())
    for i in range(n):
        num = int(input())
        if num in possibilities:
            print(num)
        else:
            diff = Math.inf
            currNum = -1
            for j in range(len(possibilities)):
                if abs(num - possibilities[j]) < diff:
                    diff = abs(num - possibilities[j])
                    currNum = possibilities[j]
            print(currNum)

main()

