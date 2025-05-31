def maxAmount(people, T):
    maxCash = 0
    possible_money = []

    for time in range(T-1, -1, -1):
        if time in people:
            for money in people[time]:
                possible_money.append(money)
        
        if possible_money:
            maxCash += max(possible_money)
            possible_money.remove(max(possible_money))
    
    return maxCash

def main():
    _input = input().split(' ')
    N = int(_input[0])
    T = int(_input[1])

    people = dict()

    for i in range(N):
        _input = input().split(' ')
        ci = int(_input[0])
        ti = int(_input[1])
        if ti not in people:
            people[ti] = []
        people[ti].append(ci)
    
    print(maxAmount(people, T))

main()