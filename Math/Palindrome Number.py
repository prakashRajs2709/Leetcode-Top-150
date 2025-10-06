class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        def helper(n):
            w = n
            m = 0
            while n>0:
                rem = n%10
                m = (m*10)+rem
                n = n//10
            return m==w
        return helper(x) 