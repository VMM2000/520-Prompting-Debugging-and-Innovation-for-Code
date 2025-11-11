def count_ways(n, m):
    # Initialize the dp matrix
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    # Set the base cases
    for i in range(n+1):
        dp[i][0] = 1
    for j in range(m+1):
        dp[0][j] = 1
    
    # Fill the dp matrix
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # Return the number of ways to fill the board
    return dp[n][m]
