
def deDuplicate(files):

    results = {}
    hashCollisions = 0
    numOfUniqueFiles = 0
    for i in range(0, len(files)):
        hashValue = Hash(files[i])

        if hashValue not in results:
            results[hashValue] = [i]
            numOfUniqueFiles += 1 
        
        else:
            flag = False
            for j in range(0, len(results[hashValue])):
                response = compareFiles(files[i], files[results[hashValue][j]])
                if not response: # Both Files are Different
                    hashCollisions += 1
                else: # Both Files are same
                    flag = True
            if not flag:
                numOfUniqueFiles += 1
                
            results[hashValue].append(i)
    return (numOfUniqueFiles, hashCollisions)


def Hash(file):
    result = ord(file[0])
    for i in range(1, len(file)):
        result = ord(file[i]) ^ result
    return result

def compareFiles(file1, file2):
    if (len(file1) != len(file2)): 
        return False
    for i in range(0, len(file1)):
        if file1[i] != file2[i]:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    inputs = []
    for i in range(0, n):
        inputs.append(input())
    result =  str(deDuplicate(inputs)).replace('(', '').replace(')','').replace(',','')
    print(result)
    
    