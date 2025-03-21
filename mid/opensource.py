# Use two dictionaries, values must be sets.


def main():
    projectDict = {}
    userDict = {}
    currProj = ''
    while True:

        _input = input()

        if _input.isdigit() and int(_input) == 0:
            break

        if _input.isdigit() and int(_input) == 1:
            # Print Everything
            sortedKeys = sorted(projectDict, key=lambda key: (-len(projectDict[key]), key))
            for Key in sortedKeys:
                print(f"{Key} {len(projectDict[Key])}")
            # Next iter
            projectDict = {}
            userDict = {}
            currProj = ''
            continue

        if _input.isupper():
            projectDict[_input] = set()
            currProj = _input

        if _input.islower():
            if _input in userDict and userDict[_input] != currProj:
                projName = userDict[_input]
                if _input in projectDict[projName]:
                    projectDict[projName].remove(_input)
                continue
            projectDict[currProj].add(_input)
            userDict[_input] = currProj
        

main()

# YOUBOOK 2
# LIVESPACE BLOGJAM 1
# UBQTS TXT 1
# SKINUX 0

# YOUBOOK 2
# UBQTS TXT 1
# LIVESPACE BLOGJAM 1
# SKINUX 0