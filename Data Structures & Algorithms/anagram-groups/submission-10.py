class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for i in strs:
            sorted_string = " ".join(sorted(i))
            ans[sorted_string].append(i)
        return list(ans.values())
            