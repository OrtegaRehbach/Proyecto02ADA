def editDistanceDP(x: str, y: str) -> int:
    '''
    Levenshtein distance or Edit distance using a Bottom-Up Dynamic Programming approach
    '''
    m, n = len(x), len(y)

    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if min(i, j) == 0:
                dp[i][j] = max(i, j)
            elif x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1],  # Replace
                                   dp[i-1][j],    # Delete
                                   dp[i][j-1]     # Insert
                                   )

    return dp[m][n]


def editDistanceDPTimeComplexity(x: int, y: int) -> int:
    '''
    Time complexity: O(m*n)
    '''
    return x * y
