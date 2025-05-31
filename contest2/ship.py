
def format_string(s):
    b = ''
    for i in range(len(s)-1, -1, -1):
        if s[i] == 'p':
            b += 'q'
        elif s[i] == 'q':
            b += 'p'
        else:
            b += s[i]
    return b


def main():
    t = int(input())
    for _ in range(t):
        a = input()
        print(format_string(a))
main()