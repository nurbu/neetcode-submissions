class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        f , e  = 0, len(s) - 1

        while f < e:
            temp = s[f]
            s[f] = s[e]
            s[e] = temp

            f += 1
            e -= 1
        