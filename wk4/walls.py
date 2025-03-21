def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5




def walls(craneRange, craneLocations, wallCentres):

    flag = False

    for i in range(len(craneLocations)):
        for j in range(len(wallCentres)):
            if euclidean_distance(craneLocations[i], wallCentres[j]) > craneRange:
                flag = False
                break
            else:
                flag = True
        if flag: 
            return 1
    


    flag = False

    for i in range(len(craneLocations)):
        for j in range(i+1, len(craneLocations)):
            for k in range(0, len(wallCentres)):
                if euclidean_distance(craneLocations[i], wallCentres[k]) > craneRange and euclidean_distance(craneLocations[j], wallCentres[k]) > craneRange:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                return 2

    flag = False

    for i in range(len(craneLocations)):
        for j in range(i+1, len(craneLocations)):
            for k in range(j+1, len(craneLocations)):
                for l in range(0, len(wallCentres)):
                    if euclidean_distance(craneLocations[i], wallCentres[l]) > craneRange and euclidean_distance(craneLocations[j], wallCentres[l]) > craneRange and euclidean_distance(craneLocations[k], wallCentres[l]) > craneRange:
                        flag = False
                        break
                    else:
                        flag = True
                if flag:
                    return 3

    flag = False

    for i in range(len(craneLocations)):
        for j in range(i+1, len(craneLocations)):
            for k in range(j+1, len(craneLocations)):
                for l in range(k+1, len(craneLocations)):
                    for m in range(0, len(wallCentres)):
                        if euclidean_distance(craneLocations[i], wallCentres[m]) > craneRange and euclidean_distance(craneLocations[j], wallCentres[m]) > craneRange and euclidean_distance(craneLocations[k], wallCentres[m]) > craneRange and euclidean_distance(craneLocations[l], wallCentres[m]) > craneRange:
                            flag = False
                            break
                        else:
                            flag = True
                    if flag:
                        return 4
    
    return 'Impossible'







def main():

    _input = input().split(' ')
    L = int(_input[0])
    W = int(_input[1])
    locationOfCranes = int(_input[2])
    craneRange = int(_input[3])

    wallCentres = []
    wallCentres.append((float(-L/2),0))
    wallCentres.append((float(L/2),0))
    wallCentres.append((0,float(-W/2)))
    wallCentres.append((0,float(W/2)))

    craneLocations = []

    for i in range(locationOfCranes):
        x, y = input().split(' ')
        craneLocations.append((int(x), int(y)))

    print(walls(craneRange, craneLocations, wallCentres))



main()