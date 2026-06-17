ipstr = input()

class Solution:
    def isValid(self, s):
        charArray = s.split('.')
        ipArray = []
        for char in charArray:
            if char == '':
                return False
            if len(char) > 1 and char[0] == '0':
                return False
            ipArray.append(int(char))
        if len(ipArray) !=4:
            return False
        for i in ipArray:
            if i > 255 or i<0:
                return False
        return True
        
print(Solution().isValid(ipstr))