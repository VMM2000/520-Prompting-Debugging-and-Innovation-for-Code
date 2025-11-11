def count_ways(n):
    dp = [[[0 for _ in range(2)] for _ in range(n + 1)] for _ in range(3 + 1)]
    for i in range(3, 0, -1):
        for j in range(n, 0, -1):
            dp[i][j][0] = 1
    for i in range(3, 0, -1):
        for j in range(n, 0, -1):
            for k in range(2):
                if k == 1:
                    dp[i][j][k] += dp[i - 1][j][0]
                    dp[i][j][k] %= 1000000007
                else:
                    dp[i][j][k] += dp[i - 1][j][1] + dp[i - 1][j - 1][0]
                    dp[i][j][k] %= 1000000007
    return dp[0][n][1]