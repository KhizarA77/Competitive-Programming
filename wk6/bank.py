# Tuple -> 0 -> Cash, 1 -> Time


def main():

    _input = input().split(' ')
    N = int(_input[0])
    T = int(_input[1])

    people = []

    for i in range(N):
        _input = input().split(' ')
        ci = int(_input[0])
        ti = int(_input[1])
        people.append((ci, ti))

    print(people)

main()