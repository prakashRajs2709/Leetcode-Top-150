from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        cur_sum = 0
        lst = []
        temp = []
        for i in nums:
            cur_sum += i
            temp.append(i)
            if cur_sum>max_sum:
                max_sum = max(max_sum,cur_sum)
                lst = temp[:]
            if cur_sum<0:
                cur_sum = 0
                temp = []
        return max_sum,lst
    
sol = Solution()
print(sol.maxSubArray(nums=[-4,3,5,2,-1]))
