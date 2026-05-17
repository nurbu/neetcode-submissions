class Solution:

    def encode(self, strs: List[str]) -> str:

        longS = []

        for i in strs:
            longS.append(str(len(i)) + "!" + i)
        return "".join(longS)

    def decode(self, s: str) -> List[str]:

        cIndex = 0

        ans = []

        while cIndex < len(s):
            
            j = cIndex 

            while s[j] != "!":
                j += 1
            wordLength = int(s[cIndex:j])
            ans.append(s[j+1:j+wordLength+1])
            cIndex = j + wordLength + 1
        return ans