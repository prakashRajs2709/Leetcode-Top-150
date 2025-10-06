class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inums=[]
        for i,n in enumerate(nums):
            inums.append((n,i))
        inums.sort()
        i=0
        j=len(inums)-1
    
        while i<j:
            inum,iindex=inums[i]
            jnum,jindex=inums[j]
            res=inum+jnum
            if res==target:
                return [iindex,jindex]
            elif res>target:
                j-=1
            else:
                i+=1
        return []
            