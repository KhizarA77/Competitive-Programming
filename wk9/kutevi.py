import math


def main():
    n, k = map(int, input().split())

    mirko_angles = list(map(int, input().split()))

    slavko_angles = list(map(int, input().split()))

    angle_gcd = 360 
    for angle in mirko_angles:
        angle_gcd = math.gcd(angle_gcd, angle)

    for angle in slavko_angles:
        if angle % angle_gcd == 0:
            print("YES")
        else:
            print("NO")

main()