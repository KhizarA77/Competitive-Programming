def max_f(n, m, reds, blues):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = max(reds[0], blues[0])
    dp[1][0] = max(reds[0], blues[0])
    for i in range(0, n):
        for j in range(0, m):
            dp[i][j] = 


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        reds = list(map(int, input().split))
        m = int(input())
        blues = list(map(int, input().split))