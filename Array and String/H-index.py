class Solution:
    def hIndex(self, nums: List[int]) -> int:
            nums.sort(reverse=True)
            res = 0
            for i,num in enumerate(nums):
                if num>=i+1:
                    res = i+1
            return res