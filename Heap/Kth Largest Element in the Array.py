class Solution:
    def findKthLargest(self, n: List[int], k: int) -> int:
        n = [-num for num in n]
        heapq.heapify(n)
        for i in range(k-1):
            -heapq.heappop(n)
        return(-heapq.heappop(n))