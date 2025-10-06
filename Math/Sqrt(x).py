class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        j=x
        while i<=j:
            mid=(i+j)//2
            mids=mid*mid
            if mids==x:
                return mid
            elif mids>x:
                j=mid-1
            else:
                i=mid+1
        return j