

def construct_b(a):
    b = []
    frequency = dict()
    curr_mode = 0
    for i in range(len(a)):
        el = a[i]
        if el not in frequency:
            frequency[el] = 1
        # You either use a[i] or you don't
        if curr_mode == el:
            pass 


def main():
    t = int(input())
    for _ in range(t):
        input()
        a = list(map(int, input().split()))