class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ma = float('-inf')
        while l<r:
            w = r-l
            h = min(height[l],height[r])
            a = w*h
            ma = max(ma,a)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ma