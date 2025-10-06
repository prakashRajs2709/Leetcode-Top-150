class Solution:
    def removeDuplicates(self, n1: List[int]) -> int:
        i = 0
        for j in range(len(n1)):
            if i<2 or n1[j]>n1[i-2]:
                n1[i] = n1[j]
                i+=1
        return i
