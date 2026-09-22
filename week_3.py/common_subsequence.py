def lcs_length(x,y):
    m,n = len(x),len(y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j] , dp[i][j+1])
    return dp[m][n]

seq1 = "ABCDEF"
seq2 = "AEBDF"
length = lcs_length(seq1,seq2)
print(f"Longest common subsequence length between '{seq1}' and '{seq2}' is : {length}")

