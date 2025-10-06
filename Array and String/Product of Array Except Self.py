class Solution:
    def productExceptSelf(self, lst: List[int]) -> List[int]:
        left = list(accumulate(lst, lambda x,y: x*y, initial=1))[:-1]
        right = list(accumulate(lst[::-1], lambda x,y: x*y, initial=1))[:-1][::-1]
        return [l*r for l,r in zip(left, right)]