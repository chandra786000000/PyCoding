s = input()

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if (n<=1):
            return s
        max_length = 1
        ans_left = 0
        ans_right = 0

        def expansion(i,j):
            left = i
            right = j
            while left>=0 and right <n and s[left]==s[right]:
                left -=1
                right +=1
            return left+1,right-1
        
        for i in range(n):
            left,right = expansion(i,i)
            if right-left+1 > max_length:
                max_length = right-left+1
                ans_left = left
                ans_right = right
            
            left,right = expansion(i,i+1)
            if right-left+1 > max_length:
                max_length = right-left+1
                ans_left = left
                ans_right = right
        return s[ans_left:ans_right+1]

print(Solution().longestPalindrome(s))

# forgeeksskeegfor
# geeksskeeg