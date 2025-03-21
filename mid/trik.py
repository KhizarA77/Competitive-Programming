def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def trik(moves):

    n = len(moves)
    Pos = [True,False,False]
    for i in range(n):
        if moves[i] == 'A':
            Pos = swap(Pos,0,1)
        elif moves[i] == 'B':
            Pos = swap(Pos,1,2)
        elif moves[i] == 'C':
            Pos = swap(Pos,0,2)
    if Pos[0]: 
        return 1
    if Pos[1]:
        return 2
    if Pos[2]:
        return 3

def main():
    moves = input()
    print(trik(moves))


main()