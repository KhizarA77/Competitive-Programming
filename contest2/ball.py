

def main():
    t = int(input())
    for _ in range(t):
        m, a, b, c = map(int, input().split())
        row1_seated = min(a, m) 
        row2_seated = min(b, m)
        
        remaining_seats = 2*m - row1_seated - row2_seated
        no_pref_seated = min(c, remaining_seats)
        
        total_monkeys = row1_seated + row2_seated + no_pref_seated
        
        print(total_monkeys)

main()
