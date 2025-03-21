import math
import sys


inputs = []

N = int(input())

for i in range(0,N):
    inputs.append(input())

def secret(N, messages):
    returnArr = []
    for i in range(0, len(messages)):
        message = messages[i]
        L = len(message)
        M = int(math.ceil(math.sqrt(L)))
        astericMessage = message + '*'*M
        matrix = [[0] * M for a in range(M)]
        counter = 0

        # Create a matrix with the stars
        for j in range(0, M):
            for k in range(0, M):
                matrix[j][k] = astericMessage[counter]
                counter += 1
        # Rotate the matrix 90 degrees clockwise
        encryptedMatrix = [[0] * M for a in range(M)]

        for j in range(0, M):
            for k in range(0, M):
                encryptedMatrix[k][M-j-1] = matrix[j][k]
                

        encryptedMessage = ''
        for j in range(0,M):
            for k in range(0, M):
                if encryptedMatrix[j][k] != '*':
                    encryptedMessage += encryptedMatrix[j][k]

        returnArr.append(encryptedMessage)         
    return returnArr

result = secret(N, inputs)
result = str(result).replace(',','\n').replace('[', '').replace(']','').replace(' ', '').replace('\'', '')
print(result)