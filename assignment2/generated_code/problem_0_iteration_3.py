def min_cost(cost, m, n):
    dp = [[float('inf')] * n for _ in range(m)]
    dp[0][0] = cost[0][0]
    for i in range(1, m):
        dp[i][0] = min(dp[i][0], dp[i - 1][0] + cost[i][0])
        for j in range(1, n):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + cost[i][j])
    return dp[m][n]