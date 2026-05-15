class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArray = [0] * 26
        tArray = [0] * 26

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sArray[ord(s[i])-ord("a")]+=1
            tArray[ord(t[i])- ord("a")]+=1
        return sArray == tArray