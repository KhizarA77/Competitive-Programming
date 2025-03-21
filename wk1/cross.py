
# rowFlag = {}
# colFlag = {}
# squareFlag = {}

# for i in range(0, 9):
#     rowFlag[i] = [False] * 10
#     colFlag[i] = [False] * 10
#     squareFlag[i] = [False] * 10

def cross(sudukoArray):
    
    rowFlag = {}
    colFlag = {}
    squareFlag = {}
    
    for i in range(0, 9):
        rowFlag[i] = [False] * 10
        colFlag[i] = [False] * 10
        squareFlag[i] = [False] * 10

    for i in range(0, 9):
        for j in range(0, 9):
            val = sudukoArray[i][j]
            if (val != 0):
                rowFlag[i][val] = True
                colFlag[j][val] = True
                boxrow = int(i/3)
                boxcol = int(j/3)
                boxIndex = boxrow*3 + boxcol
                squareFlag[boxIndex][val] = True
    
    return (squareFlag)

# print(rowFlag)
# print(colFlag)
# print(squareFlag)

inputArray = [
    [0,0,9,0,0,0,0,0,0],
    [0,0,0,0,0,4,0,0,0],
    [0,0,0,0,0,0,0,4,0],
    [0,0,0,0,0,0,0,0,0],
    [0,4,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]
print(cross(inputArray))

