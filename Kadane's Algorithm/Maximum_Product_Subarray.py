class Solution:
    def maxProduct(self, nums) -> int:
        max_prod = cur_prod = result = nums[0]
        for i in nums[1:]:
            cand = (i,max_prod*i,cur_prod*i)
            max_prod = max(cand)
            cur_prod = min(cand)
            result = max(max_prod,result)
        return result
sol = Solution()
print(sol.maxProduct(nums = [-3,-1,-1]))
