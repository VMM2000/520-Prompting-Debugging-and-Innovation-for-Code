def count_ways(n):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[n][0] = 1
    for i in range(n - 1, -1, -1):
        dp[i][0] = 1
        for j in range(1, i + 1):
            dp[i][j] = dp[i + 1][j]
            if j >= 2:
                dp[i][j] += dp[i][j - 2]
    return dp[0][n]