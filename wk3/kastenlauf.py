def manhattanDistance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def kastenlauf(inputs):
    
    visited = [False] * len(inputs)
    visited[0] = True
    queue = []
    queue.append(0)

    while queue:

        curr = queue.pop(0)

        if curr == len(inputs)-1:
            return 'happy'
        
        for i in range(0, len(inputs)):
            if not visited[i] and manhattanDistance(inputs[curr][0], inputs[curr][1], inputs[i][0], inputs[i][1]) <= 1000:
                visited[i] = True
                queue.append(i)

    return 'sad'

def main():
    numOfTestCases = int(input())

    for i in range(numOfTestCases):

        numOfStores = int(input())
        inputs = []
        for i in range(0, numOfStores+2):
            _input = input().split(' ')
            x = int(_input[0])
            y = int(_input[1])
            inputs.append((x, y))
        print(kastenlauf(inputs))

main()