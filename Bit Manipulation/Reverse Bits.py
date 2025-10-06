class Solution:
    def reverseBits(self, n: int) -> int:
        s=f'{n:032b}'
        s=s[::-1]
        n=int(s,2)
        return n
        