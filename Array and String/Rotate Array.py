class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        k = k%len(arr)
        def helper(arr,s,e):
            while s<e:
                arr[s],arr[e] = arr[e],arr[s]
                s+=1
                e-=1
        
        helper(arr,0,len(arr)-1)
        helper(arr,0,k-1)
        helper(arr,k,len(arr)-1)