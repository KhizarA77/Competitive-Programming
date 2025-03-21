def communication(byteDict):

    mapping = dict()

    for i in range(0, 256):
        val = i
        shifted_val = i << 1
        shifted_val = shifted_val & 0xFF
        encoded_val = val ^ shifted_val

        if (encoded_val in byteDict):
            mapping[encoded_val] = i



    return mapping


bytedict = set()
numOfBytes = int(input())
_input = input().split(' ')

for i in range(numOfBytes):
    val = int(_input[i])
    bytedict.add(val)

result = communication(bytedict)
output = []

for i in range(numOfBytes):
    val = int(_input[i])
    decoded_val = result[val]
    output.append(decoded_val)

print(str(output).replace('[', '').replace(']', '').replace(',',''))