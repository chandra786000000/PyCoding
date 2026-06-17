#User function Template for python3
class Solution:
    def numberOfPaths(self, m, n):
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
		        
		        
"""
The task is to count all the possible paths from top left to bottom right of a m X n matrix with the constraints that from each cell you can either move only to right or down.

Examples :

Input: m = 2, n = 2
Output: 2 
Explanation: Two possible ways are RD and DR.  
Input: m = 3, n = 3
Output: 6
Explanation: Six possible ways are RRDD, DDRR, RDDR, DRRD, RDRD, DRDR. 
Constraints:
1 <= m <= 17
1 <= n <=17
"""