class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strList = s.strip()
        if len(pattern) != len(strList):
            return False
        dictionary, rev_dicrtionary = {},{}
        for p,w in zip(pattern,strList):
            if p in dictionary and rev_dicrtionary[w] != p:
                return False
            if w in rev_dicrtionary and dictionary[p] != w:
                return False

            dictionary[p] = w
            rev_dicrtionary[w] = p
        return True

if __name__ == 'main':
    s1 = "abba"
    s2 = "dog cat cat dog"
    print(Solution().wordPattern(s1,s2))
