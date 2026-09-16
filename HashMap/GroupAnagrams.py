class Solution:
    def sign(self, s:str) ->str:
        return ''.join(sorted(s))
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        n = len(strs)
        if n == 0:
            return [[""]]
        mapStr = {}
        for s in strs:
            tmp = self.sign(s)
            if tmp not in mapStr:
                mapStr[tmp] = []
            mapStr[tmp].append(s)
        ans = []
        for k in mapStr:
            ans.append(mapStr[k])
        return ans