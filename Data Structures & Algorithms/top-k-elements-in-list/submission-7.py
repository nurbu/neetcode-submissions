class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]

        sorted_nums = {}

        for i in nums:
            sorted_nums[i] = sorted_nums.get(i,0) + 1
        ans = []
        for key,value in sorted_nums.items():
            bucket[value].append(key)
        for i in range(len(bucket)-1,-1,-1):
            current_list = bucket[i]
            for i in current_list:
                if len(ans) < k:
                    ans.append(i)
        return ans