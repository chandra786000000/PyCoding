"""
Given a number n. Find the minimum number of operations required to reach n starting from 0. You have two operations available:

Double the number
Add one to the number
Example 1:

Input: n = 8
Output: 4
Explanation: 0 + 1 = 1 --> 1 + 1 = 2 --> 2 * 2 = 4 --> 4 * 2 = 8.
Example 2:

Input: n = 7
Output: 5
Explanation: 0 + 1 = 1 --> 1 + 1 = 2 --> 1 + 2 = 3 --> 3 * 2 = 6 --> 6 + 1 = 7.
Constraints:
1 <= n <= 106
"""

class Solution:
    def minOperation(self, n):
        if n<4:
            return n
        return self.minOperation(n//2)+(n%2)+1
    
# Recursion here is faster than building DP array beause in each recusion i am only going in 1 breadth.