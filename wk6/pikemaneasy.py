def problemsSolved(times, timeLimit):
    times.sort()
    solved = 0
    penalty = 0
    time = 0
    i = 0
    while i < len(times):
        if time + times[i] > timeLimit:
            break
        solved += 1
        time += times[i]
        penalty += time
        i += 1

    penalty = penalty % 1000000007
    return (solved, penalty)


def main():
    _input = input().split(' ')
    N = int(_input[0])
    T = int(_input[1])
    _input = input().split(' ')
    A = int(_input[0])
    B = int(_input[1])
    C = int(_input[2])
    t0 = int(_input[3])
    times = []
    times.append(t0)
    for i in range(1, N):
        ti = ((A*times[i-1] + B) % C) + 1
        times.append(ti)
    print(str(problemsSolved(times, T)).replace(',','').replace('(','').replace(')',''))
main()
