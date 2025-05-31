

def main():
    PriceOfOne = int(input().split(' ')[1])
    studentsListening = list(map(int, input().split()))
    profits = [studentsListening[i] - PriceOfOne for i in range(len(studentsListening))]
    prefsum = [0] * len(profits)
    prefsum[0] = profits[0]
    max_val = 0
    for i in range(1, len(profits)):
        prefsum[i] = max(profits[i], + profits[i] + prefsum[i-1])
        max_val = max(max_val, prefsum[i])
    print(max_val)
main()