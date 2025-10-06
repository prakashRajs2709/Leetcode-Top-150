class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        mm=float('-inf')
        while i<=j:
            cm=max(nums[i],nums[j])
            mm=max(mm,cm)
            i+=1
            j-=1
        return nums.index(mm)
    
            
        