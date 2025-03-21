import math

inputs = []

inputs.append(input())
inputs.append(input())

l1 = list(map(int, inputs[0].split()))
l2 = list(map(int, inputs[1].split()))


def flex(l1, l2):
    width = l1[0]
    numOfPartitions = l1[1]

    output = [width]

    for i in range(0,numOfPartitions):
        if width - l2[i] not in output:
            output.append(width - l2[i])
        if l2[i] not in output:    
            output.append(l2[i])
        for j in range(i+1, numOfPartitions):
            if int(math.fabs(l2[j] - l2[i])) not in output:
                output.append(int(math.fabs(l2[j] - l2[i])))


    output.sort()
    return output

result = flex(l1,l2)
result = ' '.join(str(result).replace(',', '').replace('[', '').replace(']', '').split())

print(result)