def min_cost(cost, m, n):
    dp = [[float('inf')] * n for _ in range(m)]
    dp[0][0] = 0
    for i in range(m):
        for j in range(n):
            dp[i][j] = cost[i][j] + dp[i][j - 1] if j > 0 else cost[i][j]
    return dp[m][n]