def min_cost(cost):
    (m, n) = (len(cost), len(cost[0]))
    dp = [[float('inf')] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = cost[i][0]
    for j in range(n):
        dp[0][j] = cost[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + cost[i][j])
    return dp[m - 1][n - 1]