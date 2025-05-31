def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = input()
        b = input()
        c = input()
        result = "NO"
        for i in range(n):
            if a[i] == b[i] and a[i] != c[i]:
                result = "YES"
                break
            for template_char in "abcdefghijklmnopqrstuvwxyz":
                if a[i] != template_char and b[i] != template_char and c[i] == template_char:
                    result = "YES"
                    break
            
            if result == "YES":
                break
        
        print(result)

main()